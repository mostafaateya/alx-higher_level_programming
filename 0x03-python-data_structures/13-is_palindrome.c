#include "lists.h"

listint_t *node_reversing_list(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * node_reversing_list - reverses nodes of a linked list
 * @head: pointer to the first node
 * Return: pointer to the reversed list
 */

listint_t *node_reversing_list(listint_t **head)
{
	listint_t *a = *head;
	listint_t *x = NULL, *y;

	while (a)
	{
		y = a->next;
		a->next = x;
		x = a;
		a = y;
	}
	*head = x;
	return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the first node
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *x, *y, *z;
	size_t n = 0, t;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	x = *head;
	while (x)
	{
		n++;
		x = x->next;
	}
	x = *head;
	for (t = 0; t < (n / 2) - 1; t++)
		x = x->next;
	if ((n % 2) == 0 && x->n != x->next->n)
		return (0);
	x = x->next->next;
	y = node_reversing_list(&x);
	z = y;
	x = *head;
	while (y)
	{
		if (x->n != y->n)
			return (0);
		x = x->next;
		y = y->next;
	}
	node_reversing_list(&z);
	return (1);
}
