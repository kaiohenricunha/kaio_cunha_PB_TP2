class Node:
    """
    Representa um nó em uma lista encadeada simples.
    Cada nó armazena um valor e um ponteiro para o próximo nó.
    """
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"{self.value}"


class LinkedList:
    """
    Implementa uma lista encadeada simples com operações básicas:
    - Inserir no início
    - Inserir no fim
    - Excluir um nó com um valor específico
    - Exibir todos os elementos da lista
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
        Se o valor não existir, a lista permanece inalterada.
        """
        current = self.head
        previous = None

        while current:
            if current.value == value:
                if previous:
                    previous.next = current.next
                else:
                    # Se o nó a ser removido é a cabeça
                    self.head = current.next
                return True  # Nó removido com sucesso
            previous = current
            current = current.next

        return False  # Valor não encontrado

    def display(self):
        """Exibe os elementos da lista."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        return " -> ".join(elements)


def main():
    ll = LinkedList()

    # Inserção no início
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(20)
    ll.insert_at_beginning(30)
    print("Após inserções no início:", ll.display())

    # Inserção no fim
    ll.insert_at_end(5)
    ll.insert_at_end(1)
    print("Após inserções no fim:", ll.display())

    # Exclusão de um valor existente
    removed = ll.delete_value(20)
    print("Exclusão de 20:", "Removido" if removed else "Não encontrado", "| Lista:", ll.display())

    # Exclusão da cabeça
    removed = ll.delete_value(30)
    print("Exclusão de 30 (cabeça):", "Removido" if removed else "Não encontrado", "| Lista:", ll.display())

    # Tentar excluir valor que não existe
    removed = ll.delete_value(999)
    print("Tentativa de exclusão de 999:", "Removido" if removed else "Não encontrado", "| Lista:", ll.display())


if __name__ == "__main__":
    main()

