#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct Node{
	char data;
	struct Node* next;
};

bool isPalindrome(struct Node **org, struct Node *reverse){
    if (reverse == NULL) return true;
    bool check = isPalindrome(org, reverse->next);
    bool ans = ((*org)->data == reverse->data);
    *org = (*org)->next;
    return ans;
}

void push(struct Node** head, char data){
    struct Node* push_node = (struct Node*) malloc(sizeof(struct Node));
	push_node->data = data;
	push_node->next = (*head);
	(*head) = push_node;
}

void testcases(char str[], bool true_ans){
    printf("Test case: %s -- ", str);
    struct Node* head = NULL;
	for (int i = 0; str[i] != '\0'; i++)
        push(&head, str[i]);
    if (head == NULL) printf("Null exception\n\n");
    else
        isPalindrome(&head, head) == true_ans ? printf("Passed\n") : printf("Failed\n");

}

int main(){
    struct Node* head = NULL;
    int i;

    //Test case 0
	char str0[] = "";
	testcases(str0, false);

    //Test case 1
	char str1[] = "a";
	testcases(str1, true);

    //Test case 2
	char str2[] = "aa";
	testcases(str2, true);

    //Test case 3
	char str3[] = "aba";
	testcases(str3, true);

    //Test case 4
    char str9[] = "ab";
    testcases(str9, false);

    //Test case 5
	char str4[] = "abc";
	testcases(str4, false);

    //Test case 6
	char str5[] = "121";
	testcases(str5, true);

    //Test case 7
	char str6[] = "$!$";
	testcases(str6, true);

    //Test case 8
	char str7[] = "$a1";
	testcases(str7, false);

    //Test case 9
	char str8[] = "Aba";
	testcases(str8, false);

	return 0;
}
