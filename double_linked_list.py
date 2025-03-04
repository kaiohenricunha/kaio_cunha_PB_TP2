class DNode:
    """
    Nó para lista duplamente encadeada.
    Cada nó armazena um valor, referência para o próximo nó e para o nó anterior.
    """
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"{self.value}"

class DoublyLinkedList:
    """
    Lista duplamente encadeada com métodos para:
      - Inserir no início
      - Inserir no fim
      - Excluir um nó de uma posição específica (0-indexado)
      - Exibir a lista em ordem direta e reversa
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, value):
        """Insere um novo nó no início da lista."""
        new_node = DNode(value)
        if not self.head:  # Lista vazia
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, value):
        """Insere um novo nó no final da lista."""
        new_node = DNode(value)
        if not self.tail:  # Lista vazia
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete_at_position(self, pos):
        """
        Exclui o nó na posição 'pos' (0-indexado).
        Retorna True se a exclusão ocorreu, ou False se a posição for inválida.
        """
        if pos < 0 or not self.head:
            return False

        current = self.head
        index = 0
        # Se for o primeiro elemento:
        if pos == 0:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return True

        while current and index < pos:
            current = current.next
            index += 1

        if not current:
            return False  # Posição inválida

        # Atualiza ponteiros dos nós adjacentes
        if current.next:
            current.next.prev = current.prev
        else:
            # Se for o último elemento, atualiza o tail
            self.tail = current.prev

        if current.prev:
            current.prev.next = current.next

        return True

    def display_forward(self):
        """Exibe os elementos da lista na ordem direta."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        return " <-> ".join(elements)

    def display_backward(self):
        """Exibe os elementos da lista na ordem reversa."""
        elements = []
        current = self.tail
        while current:
            elements.append(str(current.value))
            current = current.prev
        return " <-> ".join(elements)

def main():
    dll = DoublyLinkedList()

    # Teste: inserção no início
    dll.insert_at_beginning(10)
    dll.insert_at_beginning(20)
    dll.insert_at_beginning(30)
    print("Após inserções no início:")
    print("Ordem direta:", dll.display_forward())
    print("Ordem reversa:", dll.display_backward())

    # Teste: inserção no fim
    dll.insert_at_end(5)
    dll.insert_at_end(1)
    print("\nApós inserções no fim:")
    print("Ordem direta:", dll.display_forward())
    print("Ordem reversa:", dll.display_backward())

    # Teste: exclusão de nó em posição específica
    # Remover o nó na posição 2 (0-indexado)
    if dll.delete_at_position(2):
        print("\nApós exclusão do nó na posição 2:")
    else:
        print("\nPosição inválida para exclusão.")
    print("Ordem direta:", dll.display_forward())
    print("Ordem reversa:", dll.display_backward())

    # Teste: exclusão do primeiro nó
    dll.delete_at_position(0)
    print("\nApós exclusão do primeiro nó:")
    print("Ordem direta:", dll.display_forward())
    print("Ordem reversa:", dll.display_backward())

    # Teste: exclusão do último nó
    # Como a lista pode ter mudado, pega a última posição contando os nós atuais
    current = dll.head
    count = 0
    while current:
        count += 1
        current = current.next
    dll.delete_at_position(count - 1)
    print("\nApós exclusão do último nó:")
    print("Ordem direta:", dll.display_forward())
    print("Ordem reversa:", dll.display_backward())

if __name__ == "__main__":
    main()

