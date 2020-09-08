#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *ptr1, *ptr2;
	int length = 0, i, j = 0;

	ptr1 = *head;
	while(ptr1)
	{
		length++;
		ptr1 = ptr1->next;
	}
	ptr1 = *head;
	for (i = 0; i < length / 2; i++)
	{
		j = 0;
		ptr2 = *head;
		while(j < (length - i - 1))
		{
			j++;
			ptr2 = ptr2->next;
		}
		if (ptr1->n != ptr2->n)
			return (0);
		ptr1 = ptr1->next;
	}
	return (1);
}
