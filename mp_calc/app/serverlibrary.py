
def mergesort(array, byfunc=None):
    p=0
    r=len(array)-1
    mergesort_recursive(array, p, r, byfunc)
    return array

def merge(array, p, q, r, byfunc):
    nleft=q-p+1
    nright=r-q
    left_array=array[p:q+1]
    right_array=array[q+1:r+1]
    left=0
    right=0
    dest=p
    if byfunc!=None:
        while (left < nleft) and (right<nright):
            if byfunc(left_array[left])<=byfunc(right_array[right]):
                array[dest]=left_array[left]
                left+=1
            else:
                array[dest]=right_array[right]
                right+=1
            dest=dest+1
        while left<nleft:
            array[dest]=left_array[left]
            left+=1
            dest+=1
        while right<nright:
            array[dest]=right_array[right]
            right+=1
            dest+=1
        return array
    else:
        while (left < nleft) and (right<nright):
            if left_array[left]<=right_array[right]:
                array[dest]=left_array[left]
                left+=1
            else:
                array[dest]=right_array[right]
                right+=1
            dest=dest+1
        while left<nleft:
            array[dest]=left_array[left]
            left+=1
            dest+=1
        while right<nright:
            array[dest]=right_array[right]
            right+=1
            dest+=1
        return array

def mergesort_recursive(array, p, r, byfunc):
    if r-p>=1:
        q=(p+r)//2
        mergesort_recursive(array, p, q, byfunc)
        mergesort_recursive(array, q+1, r, byfunc)
        merge(array, p, q, r, byfunc)
        
    return array

class Stack:
  def __init__(self):
        self.__items = []
        
  def push(self, item):
      self.__items.append(item)

  def pop(self):
      if len(self.__items)>=1: 
          return self.__items.pop()

  def peek(self):
      if len(self.__items)>=1:
          return self.__items[-1]

  @property
  def is_empty(self):
      return self.__items==[]

  @property
  def size(self):
      return len(self.__items)

class EvaluateExpression:
    valid_char = '0123456789+-*/() '
    operands = "0123456789"
    operators = "(+-*/"
    
    def __init__(self, string=""):
        self.expression=string
        self.stack = Stack()
    
    @property
    def expression(self):
        return self.expr
    
    @expression.setter
    def expression(self, new_expr):
        if isinstance(new_expr, str):
            for i in new_expr:
                if i not in self.valid_char:
                    self.expr=""
                    return self.expr
            self.expr=new_expr
            return self.expr
        self.expr=""
        return self.expr
    
    def insert_space(self):
        res=""
        for val in self.expression:
            if val in self.operands:
                res+=val
            else:
                res=res+" "+val+" "             
        return res
        
    def process_operator(self, operand_stack, operator_stack):
        right=int(operand_stack.pop())
        left=int(operand_stack.pop())
        operator=str(operator_stack.pop())
        if operator=="+":
            res=right+left
        elif operator=="-":
            res=left-right
        elif operator=="*":
            res=left*right
        else:
            res=left//right
        operand_stack.push(str(res))


    def evaluate(self):
        operand_stack = Stack()
        operator_stack = Stack()
        expression = self.insert_space()
        tokens = expression.split()
        
        for val in self.expression:
            
            if val in self.operands:
                operand_stack.push(val)
            
            elif val=="+" or val=="-":
                while not operator_stack.is_empty and (operator_stack.peek()!="(" and operator_stack.peek()!=")"):
                    self.process_operator(operand_stack, operator_stack)
                operator_stack.push(val)
            
            elif val=="*" or val=="/":  
                while not operator_stack.is_empty and (operator_stack.peek()=="*" or operator_stack.peek()=="/"):
                    self.process_operator(operand_stack, operator_stack)
                operator_stack.push(val)
            
            elif val=="(":
                operator_stack.push(val)
            
            elif val==")":
                while operator_stack.peek()!="(":
                    self.process_operator(operand_stack, operator_stack)  
                operator_stack.pop()

#             print(operand_stack.peek())
#             print(operator_stack.peek())
#             print("----")
                
        while not operator_stack.is_empty:
            self.process_operator(operand_stack, operator_stack)
        return int(operand_stack.peek())


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





