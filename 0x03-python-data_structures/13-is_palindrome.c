#include "lists.h"

/**
  * is_palindrome - This function checks if a list is a palindrome.
  * @head: The pointer head of the list.
  * Return: 0 if list not a palindrome, 1 if it is.
  */
int is_palindrome(listint_t **head)
{
	listint_t *aux = *head;
	int nodes = 0, i = 0, *arr = NULL;

	if (*head == NULL || head == NULL || (*head)->next == NULL)
		return (1);
	while (aux)
	{
		nodes++;
		aux = aux->next;
	}
	arr = malloc(sizeof(int) * nodes);
	aux = *head;
	while (aux)
	{
		arr[i++] = aux->n;
		aux = aux->next;
	}
	for (i = 0; i < nodes / 2; i++)
	{
		if (arr[i] != arr[nodes - 1 - i])
		{
			free(arr);
			return (0);
		}
	}
	free(arr);
	return (1);
}
