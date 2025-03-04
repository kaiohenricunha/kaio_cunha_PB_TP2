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
    Lista duplamente encadeada com métodos para inserção, exibição,
    ordenação via Insertion Sort e mesclagem com outra lista ordenada.
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, value):
        """Insere um novo nó com o valor dado no final da lista."""
        new_node = DNode(value)
        if not self.head:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def display_forward(self):
        """Retorna uma string com os elementos da lista na ordem direta."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        return " <-> ".join(elements)

    def display_backward(self):
        """Retorna uma string com os elementos da lista na ordem reversa."""
        elements = []
        current = self.tail
        while current:
            elements.append(str(current.value))
            current = current.prev
        return " <-> ".join(elements)

    def insertion_sort(self):
        """
        Ordena a lista duplamente encadeada usando o algoritmo Insertion Sort.
        O algoritmo percorre a lista e insere cada elemento na posição correta.
        """
        if not self.head or not self.head.next:
            return  # Lista vazia ou com um único elemento já está ordenada

        current = self.head.next
        while current:
            key_node = current
            compare = current.prev
            # Enquanto houver um nó anterior e o valor do key_node for menor,
            # move o key_node para a esquerda.
            while compare and key_node.value < compare.value:
                # Troca os valores dos nós (alternativa para reencadear nós)
                key_node.value, compare.value = compare.value, key_node.value
                key_node = compare
                compare = compare.prev
            current = current.next

    @staticmethod
    def merge_sorted(list1, list2):
        """
        Mescla duas listas duplamente encadeadas já ordenadas em uma nova lista ordenada.
        Retorna a nova lista mesclada.
        """
        merged = DoublyLinkedList()
        current1 = list1.head
        current2 = list2.head

        while current1 and current2:
            if current1.value <= current2.value:
                merged.insert_at_end(current1.value)
                current1 = current1.next
            else:
                merged.insert_at_end(current2.value)
                current2 = current2.next

        # Insere os nós restantes, se houver
        while current1:
            merged.insert_at_end(current1.value)
            current1 = current1.next
        while current2:
            merged.insert_at_end(current2.value)
            current2 = current2.next

        return merged

def main():
    # Teste do Insertion Sort em uma lista duplamente encadeada
    dll = DoublyLinkedList()
    for value in [7, 3, 9, 1, 5, 4]:
        dll.insert_at_end(value)

    print("Lista original:")
    print(dll.display_forward())

    dll.insertion_sort()
    print("\nLista ordenada (Insertion Sort):")
    print(dll.display_forward())

    # Teste da função de mesclagem
    # Cria duas listas ordenadas
    dll1 = DoublyLinkedList()
    for value in [1, 4, 7, 10]:
        dll1.insert_at_end(value)

    dll2 = DoublyLinkedList()
    for value in [2, 3, 8, 9]:
        dll2.insert_at_end(value)

    print("\nLista ordenada 1:")
    print(dll1.display_forward())
    print("Lista ordenada 2:")
    print(dll2.display_forward())

    merged = DoublyLinkedList.merge_sorted(dll1, dll2)
    print("\nLista mesclada (ordenada):")
    print(merged.display_forward())

if __name__ == "__main__":
    main()

