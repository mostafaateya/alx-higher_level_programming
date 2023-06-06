#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the first node
 * @number: input needed to insert
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *x = *head, *n;

	n = malloc(sizeof(listint_t));
	if (n == NULL)
		return (NULL);
	n->n = number;
	if (x == NULL || x->n >= number)
	{
		n->next = x;
		*head = n;
		return (n);
	}
	while (x && x->next && x->next->n < number)
		x = x->next;
	n->next = x->next;
	x->next = n;
	return (n);
}
