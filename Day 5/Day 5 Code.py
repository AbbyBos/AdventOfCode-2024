source = 'Day 5\Day 5 Prod.txt'
printing_rules = []
manual_updates = []

def importfile(source):
    with open(source, "r") as f:
        lines = f.read().splitlines()
        for row in lines:
            if len(row) == 5:
                printing_rules.append(row.split('|'))
            elif row == '':
                pass
            else:
                manual_updates.append(row.split(','))
    return printing_rules, manual_updates

def check_printing_order(manual_updates, printing_rules):
    correctly_ordered_updates = []
    incorrectly_ordered_updates = []
    middle_page_sum_correct = 0
    middle_page_sum_incorrect = 0

    for update in manual_updates:
        update = [int(x) for x in update]
        is_correct_order = True
        for i in range(len(update)):
            for j in range(i + 1, len(update)):
                page1 = str(update[i])
                page2 = str(update[j])
                
                if any(rule[1] == page1 and rule[0] == page2 for rule in printing_rules):
                    is_correct_order = False
                    break 
            if not is_correct_order:
                break 

        if is_correct_order:
            correctly_ordered_updates.append(update)
            middle_index = len(update) // 2
            middle_page_sum_correct += update[middle_index]
        else:
            incorrectly_ordered_updates.append(update)


    return correctly_ordered_updates, middle_page_sum_correct, incorrectly_ordered_updates


def order_updates(updates, rules):
    ordered_updates = []
    for update in updates:
        ordered_update = []
        available_pages = update.copy()  # Pages yet to be placed in order

        while available_pages:
            found_page = False
            for page in available_pages:
                can_place = True
                for other_page in available_pages:
                    if page != other_page:
                        if any(str(other_page) == rule[0] and str(page) == rule[1] for rule in rules):
                            can_place = False
                            break
                if can_place:
                    ordered_update.append(page)
                    available_pages.remove(page)
                    found_page = True
                    break

            if not found_page:  # Handle cases where no suitable page is found (due to incomplete or ambiguous rules)
                ordered_update.extend(available_pages)  # Just append the remaining pages arbitrarily
                available_pages.clear()

        ordered_updates.append(ordered_update)
    return ordered_updates

printing_rules, manual_updates = importfile(source)
correctly_ordered_updates, middle_page_sum_correct, incorrectly_ordered_updates = check_printing_order(manual_updates, printing_rules)

ordered_incorrect_updates = order_updates(incorrectly_ordered_updates, printing_rules)
middle_page_sum_incorrect = sum(update[len(update) // 2] for update in ordered_incorrect_updates)


print("Sum of middle page numbers (correctly ordered):", middle_page_sum_correct)
print("Sum of middle page numbers (incorrectly ordered, then corrected):", middle_page_sum_incorrect)
