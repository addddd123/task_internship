from PyQt5.QtWidgets import QApplication,QWidget ,QDialog ,  QMainWindow ,QLabel, QPushButton ,QVBoxLayout ,QHBoxLayout ,QGridLayout ,QGroupBox,QRadioButton
import  sqlite3
import os
class model1:
    def new_index(self,argu):
        db_exists=not os.path.exists('steel_sections.sqlite')
    
        if db_exists==False:
            
            conn = sqlite3.connect('steel_sections.sqlite')
            cursor = conn.cursor()
            if argu=="Channels":
              
                return conn ,cursor,cursor.execute('''SELECT COUNT(*) FROM Channels''').fetchone()[0]+1,True
                
            elif argu=="Beams":
                return conn ,cursor,cursor.execute('''SELECT COUNT(*) FROM Beams''').fetchone()[0]+1,True
            else:
                return conn ,cursor,cursor.execute('''SELECT COUNT(*) FROM Angles ''').fetchone()[0]+1,True
        else:
        #     self.genrate_msg("not_exist")
            
            return (0,0,0,False)
    def genrate_msg(self,index,db_stats=True,count_miss_value=""):
       
        dg1=QDialog()
        dg1.setWindowTitle("Database message")
        dg1.resize(170, 170)
        if db_stats==False:
            label__warn=QLabel("Database not found!!!!!!!")
            dg1.setStyleSheet("font-size:35px;"
                                    "color: red;"
                                    "background-color: white;"
                                    "font: SanSerif; "
                                    )
        elif db_stats==True :
            label__warn=QLabel("Data inserted at index "+str(index)+"\n\nBut u have not entered "+str(count_miss_value)+" values ")
            dg1.setStyleSheet("font-size:32px;"
                                    "color: blue;"
                                    "background-color: white;"
                                    "font: SanSerif; "
                                    )
                
        dg1.setLayout(QVBoxLayout())
        dg1.layout().addWidget(label__warn)
        dg1.exec_()
    def insert(self,index,know_in_which_table,get_data):
        count_empty=0
        for i in get_data:
            if i=='':
                count_empty+=1
   
        if know_in_which_table=="Channels":
          
            
        
            index[1].execute('''INSERT INTO Channels (Designation,Mass,Area,D,B,tw,T,FlangeSlope,R1,R2,Iz,Iy,rz,ry,
                                    Zz,zy,Zpz,Zpy,Source) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                  (get_data[0],get_data[1],get_data[2],get_data[3],get_data[4]
                           ,get_data[5],get_data[6],get_data[7],get_data[8],get_data[9],get_data[10],get_data[11],
                           get_data[12],get_data[13],get_data[14],get_data[15],get_data[16],get_data[17],get_data[18]))
            index[0].commit()
            index[1].close()
            index[0].close()             
            return count_empty                                                  
            
        elif know_in_which_table=="Beams":
            
            index[1].execute('''INSERT INTO Beams (Designation,Mass,Area,D,B,tw,T,FlangeSlope,R1,R2,Iz,Iy,rz,ry,
                                    Zz,zy,Zpz,Zpy,Source) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                  (get_data[0],get_data[1],get_data[2],get_data[3],get_data[4]
                           ,get_data[5],get_data[6],get_data[7],get_data[8],get_data[9],get_data[10],get_data[11],
                           get_data[12],get_data[13],get_data[14],get_data[15],get_data[16],get_data[17],get_data[18]))
            index[0].commit()
            index[1].close()
            index[0].close()  
            return count_empty
        else:
            
            index[1].execute('''INSERT INTO Angles (Designation,Mass,Area,AXB,t,R1,R2,Cz,Cy,'Tan?',Iz,Iy,'Iu(max)'
                                  ,'Iv(min)',rz,ry,'ru(max)','rv(min)',Zz,Zy,Zpz,Zpy,Source) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
                                  ,?,?,?)''',
                  (get_data[0],get_data[1],get_data[2],get_data[3],get_data[4]
                           ,get_data[5],get_data[6],get_data[7],get_data[8],get_data[9],get_data[10],get_data[11],
                           get_data[12],get_data[13],get_data[14],get_data[15],get_data[16],get_data[17],get_data[18]
                           ,get_data[19],get_data[20],get_data[21],get_data[22]))
            index[0].commit()
            index[1].close()
            index[0].close()              
            return count_empty
    def append_in_channel_database(self,get_data):
         #claculates new pk where new data will b inserted
       
        index=self.new_index("Channels")
        
        if index[3]==True:
            self.count_miss=self.insert(index,"Channels",get_data)
           
            self.genrate_msg(index[2],True,self.count_miss) #index[2] ? bkz i am returning above 3 args so tuple will be returned
        else :
            self.genrate_msg(index[2],False)
    def append_in_beams_database(self,get_data):
    
        index=self.new_index("Beams")
        if index[3]==True:
            self.count_miss=self.insert(index,"Beams",get_data)
          
            self.genrate_msg(index[2],True,self.count_miss)  #index[2] ? bkz i am returning above 3 args so tuple will be returned
        else:    
            self.genrate_msg(index[2],False)
    def append_in_angle_database(self,get_data):
        index=self.new_index("Angles ")
        if index[3]==True:
            self.count_miss=self.insert(index,"Angles ",get_data)
           
            self.genrate_msg(index[2],True,self.count_miss)#index[2] ? bkz i am returning above 3 args so tuple will be returned
        else:
            self.genrate_msg(index[2],False)