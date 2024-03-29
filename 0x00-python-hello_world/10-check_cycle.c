#include "lists.h"

/**
 * check_cycle -  checks if a singly linked list has a cycle in it
 * @list: head pointer of list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list == NULL)
		return (0);

	fast = slow = list;

	while (fast != NULL && slow != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;

		 if (fast == slow)
                {
                        return (1);
                }
	}
	return (0);

}
