#include "lists.h"

/**
 * insert_node - inserts node in list
 *
 * @head: beginning of list
 * @number: value to add
 *
 * Return: address or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new, *ptr;

if (head == NULL)
return (NULL);
new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);
ptr = *head;
if (ptr != NULL && ptr->n < number)
{
while (ptr->next != NULL && ptr->next->n < number)
ptr = ptr->next;
new->next = ptr->next;
ptr->next = new;
}
else
{
new->next = *head;
*head = new;
}
new->n = number;
return (new);
}
