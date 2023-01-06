"""
Here are all the nodes of the story as Node class instances. The parameters define the story.
text is the main text of the node that will be displayed in the main box
name is the name of the node, like an ID of the node. Must be unique.
actions is a dictionary with as keys the action words to highlight in purple and the name of the corresponding node
as value.
informative is a dictionary with as keys the informative words to highlight in green and as values the corresponding
text
"""
from node_class import Node

nodes_list = [
    Node(text="this is the first test node. The next one will be the second test",
         name="test",
         actions={
             "second test": "test2",
         },
         informative={
             "first": "Wow, are you surprised i'm going to write the word test again? Test."
         }
         ),

    Node(text="this is the second test node. The next one will be the third test. The previous one is the first",
         name="test2",
         actions={
             "third test": "test3",
             "first": "test",
         },
         informative={
             "second": "Hey, Test is forever, right? Test.",
         }
         ),

    Node(text="this is the third test node. The previous one is the second.",
         name="test3",
         actions={
             "second": "test2"
         },
         informative={
             "third": "Test for life man! The Testcode!"
         }
         ),

]
