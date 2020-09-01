#include "lists.h"

/**
 * insert_node - adds a new node to sorted list
 * @head: head of list
 * @number: value of new node
 * Return: new node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *here, *ptr;

	if (head == NULL)
		return (NULL);
	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;
	if (*head == NULL)
	{
		*head = node;
		node->next = NULL;
		return (node);
	}
	if (number < (*head)->n)
	{
		node->next = *head;
		*head = node;
		return (node);
	}
	here = *head;
	ptr = here->next;
	while (ptr)
	{
		if (number < ptr->n)
		{
			here->next = node;
			node->next = ptr;
			return (node);
		}
		here = here->next;
		ptr = ptr->next;
	}
	here->next = node;
	node->next = NULL;
	return (node);
}
