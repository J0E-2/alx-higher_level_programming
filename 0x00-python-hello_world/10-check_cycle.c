#include "lists.h"

/**
 * check_cycle -  checks if a singly linked list has a cycle in it
 * @list: head pointer of list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *temp, *temp2;

	if (list == NULL)
		return (0);

	temp = temp2 = list;

	while (temp !=  NULL)
	{
		temp2 = temp;

		while (temp2 != NULL)
		{
			if (temp == temp2->next)
			{
				return (1);
			}
			temp2 = temp2->next;
		}

		temp =  temp->next;
	}

	return (0);
}
