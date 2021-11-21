#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listsint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Descripttion: singly linked list node structure
 *
 */

 typedef struct listsint_s
 {
   int n;
   struct listsint_s *next; 
 } listint_t;

size_t print_listint(const listsint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listsint(listint_t *head);
int check_cycle(listint_t *list);


#endif /* LISTS_H */
