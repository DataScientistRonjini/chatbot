# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class SetEntity(Action):

    def name(self) -> Text:
        return "set_entity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Get the value of the entity from the user message
        entity_value = tracker.latest_message['entities'][0]['value']
        
        # dispatcher.utter_message(text=f"Yeah sure we can give you that information too.")

        return [SlotSet("person", entity_value)]
    
class CustomUtterIndividualMonthlyLateCounts(Action):

    def name(self) -> Text:
        return "custom_utter_individual_monthy_late_counts"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get the value of the slot
        slot_value = tracker.get_slot("person")
        
        # Use the value of the slot in the response
        dispatcher.utter_message(text=f"{slot_value} has come late 3 times this month.")

        return []

# class CustomUtterIndividualYearlyLateCounts(Action):

#     def name(self) -> Text:
#         return "custom_utter_individual_yearly_late_counts"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         # Get the value of the slot
#         slot_value = tracker.get_slot("person")
        
#         # Use the value of the slot in the response
#         dispatcher.utter_message(text=f"{slot_value} has come late 5 times this month.")

#         return []


