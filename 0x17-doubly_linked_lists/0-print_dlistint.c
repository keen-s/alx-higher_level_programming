#include "lists.h"
/**
*Write a function that prints all the elements of a dlistint_t list.

*Prototype: size_t print_dlistint(const dlistint_t *h);
*Return: the number of nodes
*Format: see example
*/
size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *current = h;
	size_t size = 0;

	while (current)
	{
		printf("%i\n", current->n);
		current = current->next;
		size++;
	}
	return (size);
}
