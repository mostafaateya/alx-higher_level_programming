#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct linked_list - singly linked list
 * @n: integer input needed
 * @next: pointer to the next node
 */

typedef struct linked_list
{
	int n;
	struct linked_list *next;
} lls;
int check_cycle(listint_t *list);

#endif
