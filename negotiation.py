import random
from functools import reduce

# Constraintクラスの実装
class Constraint:
    def __init__(self, id, issues, value):
        self.id = id
        self.issues = issues
        self.value = value
    def satisfy(self, aContract):
        self.id = id
        #Ex aContract = [1,3,4]
        #self.issuesの要素の数とaContractの要素の数は同じ出なければならない
        if(len(self.issues) != len(aContract)):
            raise Exception('The num of Issues in this Constraint is different from the num of issues in a Contract')
        # inside関数の実装
        # a_contract_valueは契約の値、a_min_max_values_of_issueはissueの最小値と最大値のリスト
        # a_contract_valueがa_min_max_values_of_issueの範囲内にあるかどうかを返す
        # 例えば、a_contract_valueが3で、a_min_max_values_of_issueが[2,5]の場合、 a_contract_valueはa_min_max_values_of_issueの範囲内にあるのでTrueを返す
        # 逆に、a_contract_valueが6で、a_min_max_values_of_issueが[2,5]の場合、 a_contract_valueはa_min_max_values_of_issueの範囲内にないのでFalseを返す
        # この関数を使って、aContractの全ての要素がself.issuesの各要素の範囲内にあるかどうかを調べる
        def inside(a_contract_value,a_min_max_values_of_issue):
            # a_contract_value = 3
            # a_min_max_values_of_issue = [2,5]
            #print(type(a_contract_value))
            #print(type(a_min_max_values_of_issue))
            if a_contract_value >= a_min_max_values_of_issue[0] and a_contract_value <= a_min_max_values_of_issue[1]:
                return True
            else:
                return False
            
        #print(list(map(inside,contract,issues))) # => 長さが違うと短い方に合わせてしまう
        return(reduce(lambda x,y: x and y, list(map(inside,aContract,self.issues))))# => 長さが違うと短い方に合わせてしまう

    def __str__(self):
        return "Constraint id:"+str(self.id)+" issues:"+str(self.issues)+" value:"+str(self.value)

'''
## Example
aIssues = [[1,4],[3,4],[2,4]]
## Issue 0 : 1 to 4, Issue 1 : 3 to 4, Issue 2 : 2 to 4 
## If the above conditions are satisfied, this Constraint has the value
aValue = 100
aConstraint = Constraint(0,aIssues,aValue)
print(aConstraint)
#print(aConstraint.satisfy([1,3,4,5])) #=> through exception #ok
print(aConstraint.satisfy([1,3,4])) #=> True #ok
#print(aConstraint.satisfy([1,3])) #=> through exception #ok
'''

import random

class Agent:
    id = 0
    # constraints can be assigned from outside
    def __init__(self,constraints):
        self.id = Agent.id
        Agent.id = Agent.id + 1
        self.constraints = constraints
    def __init__(self,constraints_num,issues_num, issue_value_max, issue_value_min,constraint_value_max,constraint_value_min):
        # constraints_num : the number of constraints; 制約の数
        # issues_num : the number of issues ; issueの数
        # issue_value_max : the max value of an issue ; issue値（各issueの満たされる範囲）の最大値
        # issue_value_min : the min value of an issue ; issue値（各issueの満たされる範囲）の最小値
        # constraint_value_max : 制約自体の値の最大値
        # constraint_value_min : 制約自体の値の最小値
        self.id = Agent.id
        Agent.id = Agent.id + 1
        # making constraints
        constraints = []
        for constraints_id in range(constraints_num):
            # 制約の範囲を設定する。各issue値（各issueの満たされる範囲）を設定
            anIssues = []
            for issues_i in range(issues_num):
                # issue値の満たされる範囲の計算方法：簡単バージョン
                # 最小値から（最大値-1)でランダムに１つ目の数値aを作成
                # a+1から最大値でランダムに２つ目の数値bを作成
                a = random.randint(issue_value_min,issue_value_max-1)
                b = random.randint(a+1,issue_value_max)
                anIssues.append([a,b])
            # 各Constraintに値を設定；強い制約には高い値、弱い制約には低い値を設定すべき（今後の課題）
            # 簡単バージョン constraint_value_max と constraint_value_minの間の値
            aConstraint = Constraint(constraints_id,anIssues,random.randint(constraint_value_min,constraint_value_max))                                                        
            constraints.append(aConstraint)
        self.constraints = constraints
    def computeUtilityOfAContract(self,aContract):
        # Ex: computeUtilityOfAContract([1,3,4]) =return=> 200 (value)
        # Ex: aContract = [1,3,4] means issue0 = 1, issue1 = 3, and issue2 = 4.
        # contractはissue valuesのベクトル
        # issue valuesのベクトルがあるconstraintを満たした場合、そのconstraintの価値が、このエージェントの効用に加算される
        # a contract is a vector of issue values
        # if a vector of issue values is satisfied by a constraint, then this agent obtains the value of that satisfied constraint. 
        utility = 0
        for aConstraint in self.constraints:
            #print(aConstraint)
            if(aConstraint.satisfy(aContract)):               
                #print("satisfied:")
                #print(aConstraint)
                utility = utility + aConstraint.value
        return utility
    def __str__(self):
        constraints_str = "constraints: \n"
        for aConstraint in self.constraints:
            constraints_str = constraints_str + str(aConstraint) + "\n"
        return "agent id:"+str(self.id)+"\n"+constraints_str

'''
# Example
agent1 = Agent(30,3,10,0,100,0)
print(agent1)

aContract = [5,5,5]
print("Length of contract:"+str(len(aContract)))
agent1.computeUtilityOfAContract(aContract)
'''
'''
# Exmple
agent1 = Agent(10,5,10,0,100,0) # 10 constraints, 5 issues, issue value range 0 to 10, constraint value range 0 to 100
#print(agent1)

aContract = [5,5,5,5,5]
print("Length of contract:"+str(len(aContract)))
agent1.computeUtilityOfAContract(aContract)
'''

# very simple mediator
from itertools import product
constraints_num = 1000 # for each
issues_num  = 3
issue_value_max = 10
issue_value_min = 0
constraint_value_max = 1000
constraint_value_min = 0
agent1 = Agent(constraints_num,issues_num,issue_value_max,issue_value_min,constraint_value_max,constraint_value_min)
agent2 = Agent(constraints_num,issues_num,issue_value_max,issue_value_min,constraint_value_max,constraint_value_min)

# 2つのエージェントの効用を計算

# 全てのcontractポイントを計算(pythonの関数productを使って、全ての組み合わせを計算)
a_List = list(range(issue_value_min,issue_value_max+1))
all_contracts = product(a_List,repeat=issues_num) # -> iteratorを返す
#list(all_contract)をすると、iteratorを使い切ってしまう。listにしておくか、iteratorをそのまま使うかにしないといけません。
#この次に以下をやると空リストが返される
#print(list(all_contracts))  # => これは空のリストになる (iteratorが周り切っちゃったから)

max_nash = 0
max_nash_contract = []
for a_contract in all_contracts:
    #print(a_contract)
    agent1_utility = agent1.computeUtilityOfAContract(a_contract)
    agent2_utility = agent2.computeUtilityOfAContract(a_contract)
    a_nash = agent1_utility * agent2_utility
    print("{:>15} : {:>15}".format(str(a_contract),str(a_nash)))
    #print(str(a_contract)+":"+str(a_nash))
    if max_nash < a_nash:
        max_nash = a_nash
        max_nash_contract = a_contract
    #print("agent1_utility:"+str(agent1_utility))
    #print("agent2_utility:"+str(agent2_utility))

print("Maximam Nash contract: "+str(max_nash_contract))
print("Maximam Nash value : "+str(max_nash))



