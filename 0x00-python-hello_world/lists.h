#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @data: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * 
 */
typedef struct listint_s {
int data;
struct listint_s *next;
} listint_t;

int check_cycle(listint_t *list);


#endif /* LISTS_H */
