#Level no. 2
# d d~ > u u~ z
from collections import OrderedDict

levelParticlesDict = OrderedDict()
levelParticlesDict["gluon1"] = {"name":"gluon1", "species":"gluon", "subspecies":"Gluon"}
levelParticlesDict["z1"] = {"name":"z1", "species":"boson", "subspecies":"Z Boson"}
levelParticlesDict["upQuark1"] = {"name":"upQuark1", "species":"fermion", "subspecies":"Up Quark"}
levelParticlesDict["upQuark2"] = {"name":"upQuark2", "species":"fermion", "subspecies":"Up Quark"}
levelParticlesDict["upQuark3"] = {"name":"upQuark3", "species":"fermion", "subspecies":"Up Quark"}
levelParticlesDict["downQuark1"] = {"name":"downQuark1", "species":"fermion", "subspecies":"Down Quark"}
levelParticlesDict["downQuark2"] = {"name":"downQuark2", "species":"fermion", "subspecies":"Down Quark"}
levelParticlesDict["downQuark3"] = {"name":"downQuark3", "species":"fermion", "subspecies":"Down Quark"}

levelInteractionsDict = OrderedDict()
levelInteractionsDict["QCDvertex1"] = {"name":"QCDvertex1", "species":"interaction", "subspecies":"QCD"}
levelInteractionsDict["QCDvertex2"] = {"name":"QCDvertex2", "species":"interaction", "subspecies":"QCD"}
levelInteractionsDict["QEDvertex1"] = {"name":"QEDvertex1", "species":"interaction", "subspecies":"QED"}

inputsDict = OrderedDict()
inputsDict["input1"] = {"name":"input1", "species":"interaction", "subspecies":"Input #1"}
inputsDict["input2"] = {"name":"input2", "species":"interaction", "subspecies":"Input #2"}

outputsDict = OrderedDict()
outputsDict["output1"] = {"name":"output1", "species":"interaction", "subspecies":"Output #1"}
outputsDict["output2"] = {"name":"output2", "species":"interaction", "subspecies":"Output #2"}
outputsDict["output3"] = {"name":"output3", "species":"interaction", "subspecies":"Output #3"}

winOrLose = [False]*4

def CheckIfWinningCondition(checkedInteractionDict):

   #Winning Condition No. 1
   if (
         checkedInteractionDict["input1"]["object"].isInputOrOutput == True and
         checkedInteractionDict["input1"]["object"].isConnected == True and
         checkedInteractionDict["input1"]["object"].connection.isQCD == True and
         checkedInteractionDict["input1"]["object"].connectionV1["subspecies"] == "Down Quark" and

         checkedInteractionDict["input2"]["object"].isInputOrOutput == True and
         checkedInteractionDict["input2"]["object"].isConnected == True and
         checkedInteractionDict["input2"]["object"].connection.isQCD == True and
         checkedInteractionDict["input2"]["object"].connectionV1["subspecies"] == "Down Quark" and

         checkedInteractionDict["QCDvertex1"]["object"].isQCD == True and
         checkedInteractionDict["QCDvertex2"]["object"].isQCD == True and
         checkedInteractionDict["QEDvertex1"]["object"].isQED == True and

         checkedInteractionDict["output1"]["object"].isInputOrOutput == True and
         checkedInteractionDict["output1"]["object"].isConnected == True and
         checkedInteractionDict["output2"]["object"].isInputOrOutput == True and
         checkedInteractionDict["output2"]["object"].isConnected == True and
         checkedInteractionDict["output3"]["object"].isInputOrOutput == True and
         checkedInteractionDict["output3"]["object"].isConnected == True 

         and
         
         (
            (
               checkedInteractionDict["output1"]["object"].connection.isQCD and
               checkedInteractionDict["output1"]["object"].connectionV1["subspecies"] == "Up Quark" and
               checkedInteractionDict["output1"]["object"].connectionV1["vertexNum"] == 1 and
            
               checkedInteractionDict["output2"]["object"].connection.isQED and
               checkedInteractionDict["output3"]["object"].connection.isQED
            )

            or

            (
               checkedInteractionDict["output2"]["object"].connection.isQCD and
               checkedInteractionDict["output2"]["object"].connectionV1["subspecies"] == "Up Quark" and
               checkedInteractionDict["output2"]["object"].connectionV1["vertexNum"] == 1 and
            
               checkedInteractionDict["output1"]["object"].connection.isQED and
               checkedInteractionDict["output3"]["object"].connection.isQED
            )

            or

            (
               checkedInteractionDict["output3"]["object"].connection.isQCD and
               checkedInteractionDict["output3"]["object"].connectionV1["subspecies"] == "Up Quark" and
               checkedInteractionDict["output3"]["object"].connectionV1["vertexNum"] == 1 and
            
               checkedInteractionDict["output1"]["object"].connection.isQED and
               checkedInteractionDict["output2"]["object"].connection.isQED
            )

         )

      ):
         return 0

   #Winning Condition No. 2
   if (
         checkedInteractionDict["input1"]["object"].isInputOrOutput == True and
         checkedInteractionDict["input1"]["object"].isConnected == True and
         checkedInteractionDict["input1"]["object"].connection.isQCD == True and
         checkedInteractionDict["input1"]["object"].connectionV1["subspecies"] == "Down Quark" and

         checkedInteractionDict["input2"]["object"].isInputOrOutput == True and
         checkedInteractionDict["input2"]["object"].isConnected == True and
         checkedInteractionDict["input2"]["object"].connection.isQCD == True and
         checkedInteractionDict["input2"]["object"].connectionV1["subspecies"] == "Down Quark" and

         checkedInteractionDict["QCDvertex1"]["object"].isQCD == True and
         checkedInteractionDict["QCDvertex2"]["object"].isQCD == True and
         checkedInteractionDict["QEDvertex1"]["object"].isQED == True and

         checkedInteractionDict["output1"]["object"].isInputOrOutput == True and
         checkedInteractionDict["output1"]["object"].isConnected == True and
         checkedInteractionDict["output2"]["object"].isInputOrOutput == True and
         checkedInteractionDict["output2"]["object"].isConnected == True and
         checkedInteractionDict["output3"]["object"].isInputOrOutput == True and
         checkedInteractionDict["output3"]["object"].isConnected == True 

         and

         (
            (
               checkedInteractionDict["output1"]["object"].connection.isQCD and
               checkedInteractionDict["output1"]["object"].connectionV1["subspecies"] == "Up Quark" and
               checkedInteractionDict["output1"]["object"].connectionV1["vertexNum"] == 2 and
            
               checkedInteractionDict["output2"]["object"].connection.isQED and
               checkedInteractionDict["output3"]["object"].connection.isQED
            )

            or

            (
               checkedInteractionDict["output2"]["object"].connection.isQCD and
               checkedInteractionDict["output2"]["object"].connectionV1["subspecies"] == "Up Quark" and
               checkedInteractionDict["output2"]["object"].connectionV1["vertexNum"] == 2 and
            
               checkedInteractionDict["output1"]["object"].connection.isQED and
               checkedInteractionDict["output3"]["object"].connection.isQED
            )

            or

            (
               checkedInteractionDict["output3"]["object"].connection.isQCD and
               checkedInteractionDict["output3"]["object"].connectionV1["subspecies"] == "Up Quark" and
               checkedInteractionDict["output3"]["object"].connectionV1["vertexNum"] == 2 and
            
               checkedInteractionDict["output1"]["object"].connection.isQED and
               checkedInteractionDict["output2"]["object"].connection.isQED
            )

         )

      ):
         return 1

   #Winning Condition No. 3
   if (
         (
            checkedInteractionDict["input1"]["object"].isInputOrOutput == True and
            checkedInteractionDict["input1"]["object"].isConnected == True and
            checkedInteractionDict["input1"]["object"].connection.isQED == True and
            checkedInteractionDict["input1"]["object"].connectionV1["subspecies"] == "Down Quark" and
            checkedInteractionDict["input1"]["object"].connectionV1["vertexNum"] == 1 and

            checkedInteractionDict["input2"]["object"].isInputOrOutput == True and
            checkedInteractionDict["input2"]["object"].isConnected == True and
            checkedInteractionDict["input2"]["object"].connection.isQCD == True and
            checkedInteractionDict["input2"]["object"].connectionV1["subspecies"] == "Down Quark" and
            checkedInteractionDict["input2"]["object"].connectionV1["vertexNum"] == 2
         )

         or

         (
            checkedInteractionDict["input1"]["object"].isInputOrOutput == True and
            checkedInteractionDict["input1"]["object"].isConnected == True and
            checkedInteractionDict["input1"]["object"].connection.isQCD == True and
            checkedInteractionDict["input1"]["object"].connectionV1["subspecies"] == "Down Quark" and
            checkedInteractionDict["input1"]["object"].connectionV1["vertexNum"] == 2 and

            checkedInteractionDict["input2"]["object"].isInputOrOutput == True and
            checkedInteractionDict["input2"]["object"].isConnected == True and
            checkedInteractionDict["input2"]["object"].connection.isQED == True and
            checkedInteractionDict["input2"]["object"].connectionV1["subspecies"] == "Down Quark" and
            checkedInteractionDict["input2"]["object"].connectionV1["vertexNum"] == 1
         )

         and

         checkedInteractionDict["QCDvertex1"]["object"].isQCD == True and
         checkedInteractionDict["QCDvertex2"]["object"].isQCD == True and
         checkedInteractionDict["QEDvertex1"]["object"].isQED == True and   

         checkedInteractionDict["output1"]["object"].isInputOrOutput == True and
         checkedInteractionDict["output1"]["object"].isConnected == True and
         (checkedInteractionDict["output1"]["object"].connection.isQCD == True or checkedInteractionDict["output1"]["object"].connection.isQED == True) and

         checkedInteractionDict["output2"]["object"].isInputOrOutput == True and
         checkedInteractionDict["output2"]["object"].isConnected == True and
         (checkedInteractionDict["output2"]["object"].connection.isQCD == True or checkedInteractionDict["output2"]["object"].connection.isQED == True) and

         checkedInteractionDict["output3"]["object"].isInputOrOutput == True and
         checkedInteractionDict["output3"]["object"].isConnected == True and 
         (checkedInteractionDict["output3"]["object"].connection.isQCD == True or checkedInteractionDict["output3"]["object"].connection.isQED == True) 

      ):
         return 2 

   #Winning Condition No. 4
   if (
         (
            checkedInteractionDict["input1"]["object"].isInputOrOutput == True and
            checkedInteractionDict["input1"]["object"].isConnected == True and
            checkedInteractionDict["input1"]["object"].connection.isQED == True and
            checkedInteractionDict["input1"]["object"].connectionV1["subspecies"] == "Down Quark" and
            checkedInteractionDict["input1"]["object"].connectionV1["vertexNum"] == 2 and

            checkedInteractionDict["input2"]["object"].isInputOrOutput == True and
            checkedInteractionDict["input2"]["object"].isConnected == True and
            checkedInteractionDict["input2"]["object"].connection.isQCD == True and
            checkedInteractionDict["input2"]["object"].connectionV1["subspecies"] == "Down Quark" and
            checkedInteractionDict["input2"]["object"].connectionV1["vertexNum"] == 1
         )

         or

         (
            checkedInteractionDict["input1"]["object"].isInputOrOutput == True and
            checkedInteractionDict["input1"]["object"].isConnected == True and
            checkedInteractionDict["input1"]["object"].connection.isQCD == True and
            checkedInteractionDict["input1"]["object"].connectionV1["subspecies"] == "Down Quark" and
            checkedInteractionDict["input1"]["object"].connectionV1["vertexNum"] == 1 and

            checkedInteractionDict["input2"]["object"].isInputOrOutput == True and
            checkedInteractionDict["input2"]["object"].isConnected == True and
            checkedInteractionDict["input2"]["object"].connection.isQED == True and
            checkedInteractionDict["input2"]["object"].connectionV1["subspecies"] == "Down Quark" and
            checkedInteractionDict["input2"]["object"].connectionV1["vertexNum"] == 2
         )

         and

         checkedInteractionDict["QCDvertex1"]["object"].isQCD == True and
         checkedInteractionDict["QCDvertex2"]["object"].isQCD == True and
         checkedInteractionDict["QEDvertex1"]["object"].isQED == True and   

         checkedInteractionDict["output1"]["object"].isInputOrOutput == True and
         checkedInteractionDict["output1"]["object"].isConnected == True and
         (checkedInteractionDict["output1"]["object"].connection.isQCD == True or checkedInteractionDict["output1"]["object"].connection.isQED == True) and

         checkedInteractionDict["output2"]["object"].isInputOrOutput == True and
         checkedInteractionDict["output2"]["object"].isConnected == True and
         (checkedInteractionDict["output2"]["object"].connection.isQCD == True or checkedInteractionDict["output2"]["object"].connection.isQED == True) and

         checkedInteractionDict["output3"]["object"].isInputOrOutput == True and
         checkedInteractionDict["output3"]["object"].isConnected == True and
         (checkedInteractionDict["output3"]["object"].connection.isQCD == True or checkedInteractionDict["output3"]["object"].connection.isQED == True) 
         
      ):
         return 3 

   else:
      return None
