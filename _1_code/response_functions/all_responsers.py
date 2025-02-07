from .identity import Identity
from .chatgpt import ChatGPT
from .dialogpt import Dialog_GPT
from .google_flan import Google_Flan_T5
from .facebook_blenderbot import Facebook_BlenderBot
from .dolly import Dolly



def get_model_and_responser(model_name):
    
    if model_name == 'chatgpt':
        responser = ChatGPT()
        response_fn = responser.chatgpt_call
    elif model_name == 'blenderbot':
        responser = Facebook_BlenderBot()
        response_fn = responser.bot_call
    elif model_name == 'flan':
        responser = Google_Flan_T5()
        response_fn = responser.flan_call
    elif model_name == 'dialogpt':
        responser = Dialog_GPT()
        response_fn = responser.dialogpt_call
    elif model_name == 'dolly':
        responser = Dolly()
        response_fn = responser.dolly_call
    else:
        print('WARNING: Returning Identity().')
        responser = Identity()
        response_fn = responser.identity_call
    
    return responser, response_fn