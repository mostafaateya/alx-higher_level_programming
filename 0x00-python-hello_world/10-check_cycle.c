#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the first node
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *this_node, *tester;

	if (list == NULL || list->next == NULL)
		return (0);
	this_node = list;
	tester = this_node->next;
	while (this_node != NULL && tester->next != NULL
			&& tester->next->next != NULL)
	{
		if (this_node == tester)
			return (1);
		this_node = this_node->next;
		tester = tester->next->next;
	}
	return (0);
}
