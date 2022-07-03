nclude "lists.h"

/**

   * check_cycle - checks for cycle in a linked list

    * @list: linked list to check

     * Return: 1 if cycle, 0 if not

      */

int check_cycle(listint_t *list)

{

		listint_t *temp1 = NULL, *temp2 = NULL;



			temp1 = list;

				temp2 = list;



					while (list)

							{

										temp2 = temp2->next;

												if (!temp1 || !temp2)

																return (0);

														if (temp2 == temp1)

																		return (1);

															}

						return (0);

}
