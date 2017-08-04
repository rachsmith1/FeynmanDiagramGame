#Level no. 1
from collections import OrderedDict

levelParticlesDict = OrderedDict()
levelParticlesDict["gluon1"] = {"name":"gluon1", "species":"gluon", "subspecies":"Gluon"}
levelParticlesDict["gluon2"] = {"name":"gluon2", "species":"gluon", "subspecies":"Gluon"}
levelParticlesDict["gluon3"] = {"name":"gluon3", "species":"gluon", "subspecies":"Gluon"}
levelParticlesDict["topQuark1"] = {"name":"topQuark1", "species":"fermion", "subspecies":"Top Quark"}
levelParticlesDict["topQuark2"] = {"name":"topQuark2", "species":"fermion", "subspecies":"Top Quark"}
levelParticlesDict["topQuark3"] = {"name":"topQuark3", "species":"fermion", "subspecies":"Top Quark"}

levelInteractionsDict = OrderedDict()
levelInteractionsDict["QCDvertex1"] = {"name":"QCDvertex1", "species":"interaction", "subspecies":"QCD"}
levelInteractionsDict["QCDvertex2"] = {"name":"QCDvertex2", "species":"interaction", "subspecies":"QCD"}

inputsDict = OrderedDict()
inputsDict["input1"] = {"name":"input1", "species":"interaction", "subspecies":"Input #1"}
inputsDict["input2"] = {"name":"input2", "species":"interaction", "subspecies":"Input #2"}

outputsDict = OrderedDict()
outputsDict["output1"] = {"name":"output1", "species":"interaction", "subspecies":"Output #1"}
outputsDict["output2"] = {"name":"output2", "species":"interaction", "subspecies":"Output #2"}

winOrLose = [False]*3

def CheckIfWinningCondition(checkedInteractionDict):

   #Winning Condition No. 1
   if (

         checkedInteractionDict["input1"]["object"].isInputOrOutput == True and
         checkedInteractionDict["input1"]["object"].isConnected == True and
         checkedInteractionDict["input1"]["object"].connection.isQCD == True and
         checkedInteractionDict["input1"]["object"].connection.typeQCD == 2 and
         checkedInteractionDict["input1"]["object"].connectionV1["subspecies"] == "Gluon" and

         checkedInteractionDict["input2"]["object"].isInputOrOutput == True and
         checkedInteractionDict["input2"]["object"].isConnected == True and
         checkedInteractionDict["input2"]["object"].connection.isQCD == True and
         checkedInteractionDict["input2"]["object"].connection.typeQCD == 2 and
         checkedInteractionDict["input2"]["object"].connectionV1["subspecies"] == "Gluon" and

         checkedInteractionDict["QCDvertex1"]["object"].isQCD == True and

         checkedInteractionDict["QCDvertex1"]["object"].isQCD == True and

         checkedInteractionDict["output1"]["object"].isInputOrOutput == True and
         checkedInteractionDict["output1"]["object"].isConnected == True and
         checkedInteractionDict["output1"]["object"].connection.isQCD == True and
         checkedInteractionDict["output1"]["object"].connection.typeQCD == 1 and
         checkedInteractionDict["output1"]["object"].connectionV1["subspecies"] == "Top Quark" and

         checkedInteractionDict["output2"]["object"].isInputOrOutput == True and
         checkedInteractionDict["output2"]["object"].isConnected == True and
         checkedInteractionDict["output2"]["object"].connection.isQCD == True and
         checkedInteractionDict["output2"]["object"].connection.typeQCD == 1 and
         checkedInteractionDict["output2"]["object"].connectionV1["subspecies"] == "Top Quark" and

         checkedInteractionDict["output1"]["object"].connectionV1["vertexNum"] != checkedInteractionDict["output2"]["object"].connectionV1["vertexNum"] 
      ):
         return 0

   #Winning Condition No. 2
   if (
         checkedInteractionDict["input1"]["object"].isInputOrOutput == True and
         checkedInteractionDict["input1"]["object"].isConnected == True and
         checkedInteractionDict["input1"]["object"].connection.isQCD == True and
         checkedInteractionDict["input1"]["object"].connection.typeQCD == 1 and
         checkedInteractionDict["input1"]["object"].connectionV1["subspecies"] == "Gluon" and

         checkedInteractionDict["input2"]["object"].isInputOrOutput == True and
         checkedInteractionDict["input2"]["object"].isConnected == True and
         checkedInteractionDict["input2"]["object"].connection.isQCD == True and
         checkedInteractionDict["input2"]["object"].connection.typeQCD == 1 and
         checkedInteractionDict["input2"]["object"].connectionV1["subspecies"] == "Gluon" and

         checkedInteractionDict["QCDvertex1"]["object"].isQCD == True and

         checkedInteractionDict["QCDvertex1"]["object"].isQCD == True and

         checkedInteractionDict["output1"]["object"].isInputOrOutput == True and
         checkedInteractionDict["output1"]["object"].isConnected == True and
         checkedInteractionDict["output1"]["object"].connection.isQCD == True and
         checkedInteractionDict["output1"]["object"].connection.typeQCD == 1 and
         checkedInteractionDict["output1"]["object"].connectionV1["subspecies"] == "Top Quark" and
         checkedInteractionDict["output1"]["object"].connectionV1["vertexNum"] == 1 and

         checkedInteractionDict["output2"]["object"].isInputOrOutput == True and
         checkedInteractionDict["output2"]["object"].isConnected == True and
         checkedInteractionDict["output2"]["object"].connection.isQCD == True and
         checkedInteractionDict["output2"]["object"].connection.typeQCD == 1 and
         checkedInteractionDict["output2"]["object"].connectionV1["subspecies"] == "Top Quark" and
         checkedInteractionDict["output2"]["object"].connectionV1["vertexNum"] == 2
      ):
         return 1

   #Winning Condition No. 3
   if (
         checkedInteractionDict["input1"]["object"].isInputOrOutput == True and
         checkedInteractionDict["input1"]["object"].isConnected == True and
         checkedInteractionDict["input1"]["object"].connection.isQCD == True and
         checkedInteractionDict["input1"]["object"].connection.typeQCD == 1 and
         checkedInteractionDict["input1"]["object"].connectionV1["subspecies"] == "Gluon" and

         checkedInteractionDict["input2"]["object"].isInputOrOutput == True and
         checkedInteractionDict["input2"]["object"].isConnected == True and
         checkedInteractionDict["input2"]["object"].connection.isQCD == True and
         checkedInteractionDict["input2"]["object"].connection.typeQCD == 1 and
         checkedInteractionDict["input2"]["object"].connectionV1["subspecies"] == "Gluon" and

         checkedInteractionDict["QCDvertex1"]["object"].isQCD == True and

         checkedInteractionDict["QCDvertex1"]["object"].isQCD == True and

         checkedInteractionDict["output1"]["object"].isInputOrOutput == True and
         checkedInteractionDict["output1"]["object"].isConnected == True and
         checkedInteractionDict["output1"]["object"].connection.isQCD == True and
         checkedInteractionDict["output1"]["object"].connection.typeQCD == 1 and
         checkedInteractionDict["output1"]["object"].connectionV1["subspecies"] == "Top Quark" and
         checkedInteractionDict["output1"]["object"].connectionV1["vertexNum"] == 2 and

         checkedInteractionDict["output2"]["object"].isInputOrOutput == True and
         checkedInteractionDict["output2"]["object"].isConnected == True and
         checkedInteractionDict["output2"]["object"].connection.isQCD == True and
         checkedInteractionDict["output2"]["object"].connection.typeQCD == 1 and
         checkedInteractionDict["output2"]["object"].connectionV1["subspecies"] == "Top Quark" and
         checkedInteractionDict["output2"]["object"].connectionV1["vertexNum"] == 1
      ):
         return 2

   else:
      return None


