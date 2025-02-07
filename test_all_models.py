from _1_code.response_functions.identity import identity
from _1_code.response_functions.dialogpt import Dialog_GPT
from _1_code.response_functions.facebook_blenderbot import Facebook_BlenderBot
from _1_code.response_functions.google_flan import Google_Flan_T5



list_modules = [Dialog_GPT, Facebook_BlenderBot]#, Google_Flan_T5]

for module in list_modules:
    module()