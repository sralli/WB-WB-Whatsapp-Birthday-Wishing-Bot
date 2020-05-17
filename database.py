import pandas as pd
from ast import literal_eval
from datetime import date

class Init_df:
    '''
        Docstring: Initializes the dataframe with the given characteristics. Retreives and fills back data in after sending the message
    '''

    def __init__(self):
        self.df = pd.DataFrame(pd.read_csv('Birthdays_Database.csv'))
        self.df.Already_Sent = self.df.Already_Sent.fillna('Temp').apply(lambda x : [] if x=='Temp' else x)
        self.names, self.today_already_sent = [], []
        try:
            self.df.Already_Sent = self.df.Already_Sent.apply(lambda x: literal_eval(x))
        except:
            pass
        
    def Birthday_Today(self):
        #Check whose birthday is today
        today = date.today().strftime("%d-%B")
        self.df_today = self.df[self.df.Birthday==today]
        self.names = list(self.df_today.Name.values)
        self.today_already_sent = list(self.df_today.Already_Sent.values)
        self.nicknames = list(self.df_today.NickName.values)
        return self.names, self.today_already_sent, self.nicknames




class Update(Init_df):
    '''
        Docstring: Updates the already sent values in the dataframe, so that the same user doesn't get the same messages
    '''

    def __init__(self, sent_value, idx):
        Init_df.__init__(self)
        self.names, self.today_already_sent, self.nicknames = Init_df.Birthday_Today(self)
        self.sent_value = sent_value
        self.idx = idx
        self.update()
    
    def update(self):
    
        try:
            self.df_today.Already_Sent = self.df_today.Already_Sent.apply(lambda x: literal_eval(x))
        except:
            pass
        self.df_today.Already_Sent.iloc[self.idx].append(int(self.sent_value))

        self.df['Already_Sent'] = self.df['Name'].map(self.df_today.set_index('Name')['Already_Sent'])
        self.df.to_csv("Birthdays_Database.csv", encoding='utf-8', index=False)