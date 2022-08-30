from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def isEmpty(self): # isEmpty - проверка стека на пустоту. Метод возвращает True или False.
        if len(self.stack) == 0:
            return True
        elif len(self.stack) > 0:
            return False

    def push(self, item): # push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
        self.stack.append(item)

    def pop(self): # pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def peek(self): # peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
        if len(self.stack) == 0:
            return None
        symbol = self.stack[-1]
        return symbol

    def size(self): # size - возвращает количество элементов в стеке.
        return len(self.stack)

def balance_check(str):
    dict_symbol = {')': '(', ']': '[', '}': '{'}
    open_symbol = dict_symbol.values()
    close_symbol = dict_symbol.keys()
    stack = Stack()
    balance = True
    index = 0
    while index < len(str) and balance:
        symbol = str[index]
        if symbol in open_symbol:
            stack.push(symbol)
        elif symbol in close_symbol:
            top = stack.pop()
            if dict_symbol[symbol] != top:
                balance = False
        index += 1
    if balance and stack.isEmpty():
        return True
    else:
        return False

if __name__ == '__main__':
    # Пример сбалансированных последовательностей скобок:
    string_1 = '(((([{}]))))'
    string_2 = '[([])((([[[]]])))]{()}'
    string_3 = '{{[(08)-9]}}'

    # Несбалансированные последовательности:
    string_4 = '{{6}'
    string_5 = '{{[(])]}}'
    string_6 = '[[{())}]'

    print(f"{string_1} - {balance_check(string_1)}")
    print(f"{string_2} - {balance_check(string_2)}")
    print(f"{string_3} - {balance_check(string_3)}")
    print(f"{string_4} - {balance_check(string_4)}")
    print(f"{string_5} - {balance_check(string_5)}")
    print(f"{string_6} - {balance_check(string_6)}")


