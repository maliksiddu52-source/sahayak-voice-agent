# Mock Database of Government Schemes

SCHEMES = [
    {
        "id": "pm_kisan",
        "name": "Pradhan Mantri Kisan Samman Nidhi (PM-KISAN)",
        "category": "Agriculture",
        "description": "Financial support of ₹6,000 per year to land-holding farmer families, payable in three equal installments of ₹2,000.",
        "benefits": "₹6,000 per year direct cash transfer.",
        "criteria": {
            "occupation": ["farmer"],
            "income_limit": 2000000, 
            "age_min": 18,
            "exclusion": "Institutional land holders, tax payers"
        }
    },
    {
        "id": "ayushman_bharat",
        "name": "Ayushman Bharat Pradhan Mantri Jan Arogya Yojana (PM-JAY)",
        "category": "Health",
        "description": "World's largest health insurance scheme providing coverage of ₹5 lakh per family per year for secondary and tertiary care hospitalization.",
        "benefits": "Free treatment up to ₹5 lakh per year in empaneled hospitals.",
        "criteria": {
            "income_limit": 250000,
            "category": ["poor", "deprived", "occupational_category_d_list"]
        }
    },
    {
        "id": "pm_awas_urban",
        "name": "Pradhan Mantri Awas Yojana (Urban)",
        "category": "Housing",
        "description": "Provides pucca houses to all eligible urban households. Includes interest subsidy on home loans.",
        "benefits": "Subsidy on home loan interest rates (CLSS) or financial assistance for house construction.",
        "criteria": {
            "location": "urban",
            "income_max": 1800000, 
            "property_ownership": "none"
        }
    },
    {
        "id": "pm_awas_rural",
        "name": "Pradhan Mantri Awas Yojana (Grameen)",
        "category": "Housing",
        "description": "Assistance for construction of a pucca house for rural families without shelter.",
        "benefits": "Financial assistance of ₹1.20 lakh (plains) or ₹1.30 lakh (hilly areas).",
        "criteria": {
            "location": "rural",
            "housing_status": "kutcha_house_or_homeless",
            "category": ["sc", "st", "minority", "others_below_poverty_line"]
        }
    },
    {
        "id": "pm_mudra",
        "name": "Pradhan Mantri MUDRA Yojana (PMMY)",
        "category": "Business/Loan",
        "description": "Loans up to ₹10 lakh to non-corporate, non-farm small/micro enterprises.",
        "benefits": "Loans in 3 categories: Shishu (up to ₹50k), Kishore (₹50k-₹5L), Tarun (₹5L-₹10L). No collateral required.",
        "criteria": {
            "occupation": ["small_business", "entrepreneur", "shopkeeper"],
            "age_min": 18
        }
    },
    {
        "id": "pm_ujjwala",
        "name": "Pradhan Mantri Ujjwala Yojana (PMUY)",
        "category": "Energy/Women",
        "description": "Free LPG gas connection to women from Below Poverty Line (BPL) households.",
        "benefits": "Free first refill and stove, deposit-free LPG connection.",
        "criteria": {
            "gender": "female",
            "age_min": 18,
            "financial_status": "bpl"
        }
    },
    {
        "id": "sukanya_samriddhi",
        "name": "Sukanya Samriddhi Yojana (SSY)",
        "category": "Child Welfare",
        "description": "A small deposit scheme for the girl child launched as a part of the 'Beti Bachao Beti Padhao' campaign.",
        "benefits": "High interest rate (approx 8%), tax benefits under 80C. Maturity at age 21.",
        "criteria": {
            "gender": "female",
            "age_max": 10
        }
    },
    {
        "id": "atal_pension",
        "name": "Atal Pension Yojana (APY)",
        "category": "Pension",
        "description": "Pension scheme for citizens of India, focused on the unorganized sector workers.",
        "benefits": "Guaranteed pension of ₹1,000 to ₹5,000 per month after age 60.",
        "criteria": {
            "age_min": 18,
            "age_max": 40,
            "employment_type": "unorganized"
        }
    },
    {
        "id": "mgnrega",
        "name": "MGNREGA",
        "category": "Employment",
        "description": "Mahatma Gandhi National Rural Employment Guarantee Act. Guarantees 100 days of wage employment.",
        "benefits": "Guaranteed 100 days of unskilled work per financial year.",
        "criteria": {
            "location": "rural",
            "age_min": 18,
            "willingness": "unskilled_manual_work"
        }
    },
    {
        "id": "pm_svanidhi",
        "name": "PM SVANidhi",
        "category": "Business/Loan",
        "description": "Micro-credit facility for street vendors.",
        "benefits": "Collateral-free working capital loan up to ₹10,000.",
        "criteria": {
            "occupation": ["street_vendor", "hawker"],
            "location": "urban"
        }
    }
]

def get_all_schemes():
    return SCHEMES

def get_scheme_by_id(scheme_id):
    for scheme in SCHEMES:
        if scheme["id"] == scheme_id:
            return scheme
    return None
