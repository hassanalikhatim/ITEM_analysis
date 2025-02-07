import os
import pandas as pd
from IPython.display import clear_output
import math



def itu_dataset_cleaning(
    data_path,
    destination_path
):
    
    df_questions = pd.read_excel(destination_path+'/Questions.xlsx', engine='openpyxl')
    df = pd.read_excel(destination_path+'/Answers2.xlsx', engine='openpyxl')
    
    current_index = -1
    data_dirs = os.listdir(data_path)
    for d, dir_ in enumerate(data_dirs):
        dir_path = data_path + dir_ + '/'
        
        number = int(dir_.split('_')[-1])
        
        scripts_names = os.listdir(dir_path)
        for s, script in enumerate(scripts_names):
            script_path = dir_path + script
            
            current_index += 1
            if current_index > len(df):
                answers_to_questions = [''] * 10
                current_question = 0
                
                text = open(script_path,'r').read()
                text = text.replace('?', '.')
                
                all_sentences = text.split('. ')
                for sentence in all_sentences:
                    clear_output(wait=True)
                    
                    question = str(current_index) + ', ' + script + ':\n'
                    print(question)
                
                    list_numbers = [str(i) for i in range(1, 11)]
                    list_appended_numbers = [str(i)+'.' for i in range(1, 11)]
                    key_ = input(sentence)
                    
                    # NEXT QUESTION AND IGNORE
                    if key_ in list_appended_numbers:
                        answers_to_questions[int(key_[:-1])-1] += sentence + '. '
                        last_key = int(key_[:-1]) - 1
                    elif key_ in list_numbers:
                        last_key = int(key_) - 1
                    elif key_ == '.':
                        flag = 'nothing'
                    else:
                        answers_to_questions[last_key] += sentence + '. '
                        
                    """
                    Only pressing enter appends the statement to the answer of the last question.
                    Entering numbers 1-10 and pressing enter changes the question to the number entered.
                    Entering numbers 1-10 with a . and pressing enter changes the question to the number entered and appends to the answer.
                    Entering . and pressing enter does nothing.
                    """
                            
                list_add = [script, number, 'CS'] + answers_to_questions + ['0']
                df.loc[current_index] = list_add
                df.to_excel(destination_path+'Answers2.xlsx', index=False)
    
    return


def remove_nan_answers(df):
    
    for n in range(len(df)):
        for a in range(1, 11):
            answer = df[n:n+1]['answer_'+str(a)].tolist()[0]
            if not isinstance(answer, str):
                if math.isnan(answer):
                    df.at[n, 'answer_'+str(a)] = 'Sorry, Sir. I don\'t know the answer to this question.'
    
    return df


def process_itu_interviews(
    filename='candidates_information',
    destination_path='',
    num_questions=10
):
    
    df = pd.read_excel(destination_path+'Answers2.xlsx', engine='openpyxl')
    questions = pd.read_excel(destination_path+'Questions.xlsx', engine='openpyxl')
    
    candidate_information = pd.DataFrame()
    
    for n in range(len(df)):    
        
        if df[n:n+1]['subject'].tolist()[0] == 'CS':
            questions_ref = 'Computer'
        elif df[n:n+1]['subject'].tolist()[0] == 'EE':
            questions_ref = 'Electrical'

        processed_response = []
        processed_response += ['Candidate Background: Religion: <religious affiliation>, Gender: <gender>, Country: <country>']
        for a in range(1, num_questions+1):
            question_to_candidate = questions[a:a+1][questions_ref].tolist()[0]
            answer_of_candidate = df[n:n+1]['answer_'+str(a)].tolist()[0]
            
            processed_response.append(
                'Question: ' + question_to_candidate + '. Answer: ' + answer_of_candidate
            )
        
        assert len(processed_response) == num_questions+1
        candidate_information['Candidate ' + str(n)] = processed_response
        
    candidate_information.to_excel(destination_path+filename+'.xlsx', index=False)
    df.to_excel(destination_path+filename+'_0.xlsx', index=False)
    
    return

