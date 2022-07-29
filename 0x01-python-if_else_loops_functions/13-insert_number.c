#include <stdlib.h>
#include "lists.h"

/**
 * *insert_node - inserts a number in a sorted singly linked list
 * @head: pointer
 * @number: integer
 * Return: address of new node, NULL upon failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *i, *temp;

	i = malloc(sizeof(listint_t));
	if (i == NULL)
		return (NULL);
	if (*head == NULL)
	{
		i->n = number;
		i->next = *head;
		*head = i;
		return (i);
	}
	else if (number <= (*head)->n)
	{
		i->n = number;
		i->next = *head;
		*head = i;
		return (i);
	}
	else
	{
		temp = *head;
		while (temp->next != NULL && number > temp->next->n)
		{
			temp = temp->next;
		}
		i->n = number;
		i->next = temp->next;
		temp->next = i;
		return (i);
	}
	return (NULL);
}
