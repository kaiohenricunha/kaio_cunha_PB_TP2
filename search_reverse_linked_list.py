class Node:
    """
    Nó de uma lista encadeada simples.
    Armazena um valor e uma referência para o próximo nó.
    """
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"{self.value}"


class LinkedList:
    """
    Lista encadeada simples com operações de inserção, exclusão, 
    busca e inversão da lista.
    """
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        """Insere um novo nó com o valor dado no início da lista."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value):
        """Insere um novo nó com o valor dado no final da lista."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_value(self, value):
        """
        Exclui o primeiro nó que contenha o valor especificado.
        Retorna True se o nó foi removido, ou False se não encontrado.
        """
        current = self.head
        previous = None

        while current:
            if current.value == value:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True
            previous = current
            current = current.next

        return False

    def display(self):
        """Retorna uma string representando os elementos da lista."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        return " -> ".join(elements)

    def search(self, value):
        """
        Busca o nó com o valor especificado.
        Retorna a posição (0-indexado) se encontrado; caso contrário, retorna -1.
        """
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            index += 1
            current = current.next
        return -1

    def reverse(self):
        """
        Inverte a lista encadeada.
        Após a inversão, o primeiro nó passa a ser o último e vice-versa.
        """
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous


def main():
    ll = LinkedList()

    # Inserções para teste
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(20)
    ll.insert_at_beginning(30)
    ll.insert_at_end(5)
    ll.insert_at_end(15)
    print("Lista original:")
    print(ll.display())

    # Teste do método search
    value = 10
    pos = ll.search(value)
    print(f"\nValor {value} encontrado na posição: {pos}" if pos != -1 else f"\nValor {value} não encontrado.")

    value = 99
    pos = ll.search(value)
    print(f"Valor {value} encontrado na posição: {pos}" if pos != -1 else f"Valor {value} não encontrado.")

    # Teste do método reverse
    ll.reverse()
    print("\nLista após inversão:")
    print(ll.display())

    # Testando a inversão em lista com um único elemento
    single_ll = LinkedList()
    single_ll.insert_at_beginning(42)
    print("\nLista com um único elemento antes da inversão:")
    print(single_ll.display())
    single_ll.reverse()
    print("Lista com um único elemento após a inversão:")
    print(single_ll.display())

if __name__ == "__main__":
    main()

