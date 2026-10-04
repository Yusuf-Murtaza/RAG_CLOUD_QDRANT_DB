"""Step 6b: Route the LLM through a portkey gateway

Instead of calling Openrouter directly, the main LLM call goes through Portkey.
Portkey stores the real Openrouter credentials behind a "slug" (set up once in
the Portkey dashboard) - our code never sees the raw Openrouter key.

NOTE on fallback: we used to send a "config" (strategy: fallback + a
list of targets) via the x-portkey-config header, either as inline JSON
or as a saved config's "pc-..." slug. This Portkey workspace has
"block_inline_config" enabled, and there's no saved config to reference
either, so ANY x-portkey-config header - inline or slug - gets rejected
with `inline_config_blocked`. Routing straight to one provider via
x-portkey-provider sidesteps the config mechanism entirely (that header
isn't validated the same way), which is why this version doesn't send a
config at all. The tradeoff: no more automatic Portkey-side fallback to
a second slug if @hrpolicy fails - see docs/05_portkey_gateway.md.
"""

import json
from langchain_openai import ChatOpenAI
from hr_assistant import config
from portkey_ai import createHeaders, PORTKEY_GATEWAY_URL
from hr_assistant.logger import get_logger

logger = get_logger(__name__)

#My main model - application

PRIMARY_PROVIDER = "@hrpolicynew"

PRIMARY_TARGET = {"provider": "@hrpolicynew", 
                  "override_params": {"model": config.LLM_MODEL_NAME}}

FALLBACK_TARGET = {"provider": "@hrpolicybackupnew", 
                  "override_params": {"model": "openai/gpt-oss-20b"}}


#We can define below config in portkey website as well instead of below to make it private.
# Defining below will make config as public.
#In portkey website we can define fallback strategy and targets. 
#Then we can use the slug of that config here instead of defining it here. 
# But for now we are defining it here.
#pc-hrpoli-10bfc9
GATEWAY_CONFIG = {
    "strategy": {
        "mode": "fallback"
    },
    "targets": [PRIMARY_TARGET, FALLBACK_TARGET]
}

#Function to access our gateway - Portkey AI
def get_gateway_llm() -> ChatOpenAI:
    """Return a chatmodel routed through portkey with automatic fallback"""
    logger.info("Routing LLM calls through Portkey (primary= @hrpolicy1, fallback= @hrpolicybackup1)")
    headers = createHeaders(
        api_key=config.PORTKEY_API_KEY, 
        config=config.PORTKEY_CONFIG_ID
    )
    return ChatOpenAI(
        api_key=config.PORTKEY_API_KEY,
        base_url=PORTKEY_GATEWAY_URL,
        default_headers=headers,
    )
