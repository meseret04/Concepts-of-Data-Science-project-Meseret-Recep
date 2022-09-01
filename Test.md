
## Inserting on the numbers file


```python
insert_list = [5, 51, 82, 98]

print(number_tree.draw_number_tree())
for i in insert_list:
    number_tree.insert(i)
    print(f'inserting {i}...')
print(number_tree.draw_number_tree())
```

    
              ___________________49_______________
             /                                    \
        ____29_________                        ____60_________
       /               \                      /               \
      15            ____36               ____57            ____84___
     /  \          /      \             /      \          /         \
    5    16      _31       43         _54       59      _71         _98
                /   \        \       /   \             /   \       /   \
               30    34       48    51    56          67    82    87    99
    
    inserting 5...
    inserting 51...
    inserting 82...
    inserting 98...
    
              ___________________49_______________
             /                                    \
        ____29_________                        ____60_________
       /               \                      /               \
      15            ____36               ____57            ____84___
     /  \          /      \             /      \          /         \
    5    16      _31       43         _54       59      _71         _98
                /   \        \       /   \             /   \       /   \
               30    34       48    51    56          67    82    87    99
    

