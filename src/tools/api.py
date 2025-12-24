"""
API Layer for Scheme Tools.
Exposes functions for the agent to call.
"""
from src.tools.schemes_db import get_all_schemes

def search_schemes(query: str):
    """
    Search for schemes based on a keyword query.
    Returns a list of matching schemes (name and description).
    """
    schemes = get_all_schemes()
    query = query.lower()
    results = []
    
    for scheme in schemes:
        if query in scheme['name'].lower() or query in scheme['description'].lower():
            results.append({
                "id": scheme['id'],
                "name": scheme['name'],
                "description": scheme['description']
            })
            
    return results

def check_eligibility(scheme_id: str, age: int, income: int, occupation: str, gender: str = "any"):
    """
    Check if a user is eligible for a specific scheme.
    """
    schemes = get_all_schemes()
    scheme = next((s for s in schemes if s['id'] == scheme_id), None)
    
    if not scheme:
        return {"eligible": False, "reason": "Scheme not found."}
        
    criteria = scheme['criteria']
    
    # Check Age
    if not (criteria['min_age'] <= age <= criteria['max_age']):
        return {"eligible": False, "reason": f"Age {age} is not within {criteria['min_age']}-{criteria['max_age']} range."}
        
    # Check Income
    if income > criteria.get('income_limit', float('inf')):
        return {"eligible": False, "reason": f"Income {income} exceeds limit {criteria['income_limit']}."}
        
    # Check Occupation
    if criteria.get('occupation') != "any" and criteria.get('occupation') != occupation:
         # Simplified check: allows 'any' or exact match
        if occupation != criteria['occupation']:
             return {"eligible": False, "reason": f"Occupation '{occupation}' does not match required '{criteria['occupation']}'."}

    # Check Gender
    if criteria.get('gender') and criteria.get('gender') != gender:
        return {"eligible": False, "reason": f"Gender '{gender}' does not match required '{criteria['gender']}'."}

    return {"eligible": True, "reason": "You meet all the criteria!"}

def get_scheme_details(scheme_id: str):
    """
    Get full details of a scheme by ID.
    """
    schemes = get_all_schemes()
    scheme = next((s for s in schemes if s['id'] == scheme_id), None)
    return scheme
