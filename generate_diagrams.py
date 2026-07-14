import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_architecture_diagram():
    fig, ax = plt.subplots(figsize=(14, 4.5))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 4.5)
    ax.axis('off')

    def draw_box(x, y, w, h, text):
        rect = patches.Rectangle((x, y), w, h, linewidth=1, edgecolor='black', facecolor='#d9e1f2')
        ax.add_patch(rect)
        ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=11, wrap=True)

    def draw_arrow(x1, y1, x2, y2, text="", rad=0.0):
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1), 
                    arrowprops=dict(arrowstyle="-|>", color="black", lw=1.5, connectionstyle=f"arc3,rad={rad}"))
        if text:
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2
            ax.text(mid_x, mid_y + 0.1, text, ha='center', va='bottom', fontsize=10)

    # Boxes
    draw_box(0.5, 1.75, 2.5, 1, "FinRelief AI\nWeb Application")

    draw_box(5, 3.2, 2.5, 0.8, "FastAPI: Backend\nFramework")
    draw_box(5, 1.85, 2.5, 0.8, "User Input")
    draw_box(5, 0.5, 2.5, 0.8, "Secure JWT &\nSQLite Database")

    draw_box(9.5, 1.85, 2.5, 0.8, "Gemini API:\nGenerative AI")

    draw_box(13, 3.2, 2, 0.7, "Settlement\nStrategies")
    draw_box(13, 1.9, 2, 0.7, "Negotiation\nLetters")
    draw_box(13, 0.6, 2, 0.7, "Financial\nInsights")

    # Arrows
    draw_arrow(3.0, 2.25, 5, 3.6, "Built With", rad=-0.1)
    draw_arrow(3.0, 2.25, 5, 2.25, "Receives")
    draw_arrow(3.0, 2.25, 5, 0.9, "Ensures", rad=0.1)

    draw_arrow(7.5, 2.25, 9.5, 2.25, "Integrates with")

    draw_arrow(12.0, 2.25, 13, 3.55, "Generates", rad=-0.1)
    draw_arrow(12.0, 2.25, 13, 2.25, "Generates")
    draw_arrow(12.0, 2.25, 13, 0.95, "Generates", rad=0.1)

    plt.tight_layout()
    plt.savefig('documentation/7.Project Documentation/Architecture_Diagram.png', dpi=300, bbox_inches='tight')
    print("Generated Architecture_Diagram.png")

def create_er_diagram():
    fig, ax = plt.subplots(figsize=(14, 5))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 5)
    ax.axis('off')

    def draw_box(x, y, w, h, title, fields):
        rect_head = patches.Rectangle((x, y+h-0.4), w, 0.4, linewidth=1, edgecolor='black', facecolor='#b4c6e7')
        ax.add_patch(rect_head)
        ax.text(x + w/2, y+h-0.2, title, ha='center', va='center', fontsize=10, fontweight='bold')
        
        rect_body = patches.Rectangle((x, y), w, h-0.4, linewidth=1, edgecolor='black', facecolor='#e9eef7')
        ax.add_patch(rect_body)
        ax.text(x + 0.1, y + (h-0.4)/2, fields, ha='left', va='center', fontsize=8, linespacing=1.6)
        return (x, x+w, y, y+h)

    def draw_rel(x1, y1, x2, y2, label="", rad=0.0):
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1), 
                    arrowprops=dict(arrowstyle="-|>", color="black", lw=1.2, connectionstyle=f"arc3,rad={rad}"))
        if label:
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2
            ax.text(mid_x, mid_y, label, ha='center', va='bottom', fontsize=8, color='#d32f2f', fontweight='bold', bbox=dict(facecolor='white', edgecolor='none', alpha=0.7, pad=0))

    # Draw Entities
    draw_box(0.5, 1.8, 2.2, 1.6, "USERS", "id (PK)\nemail\nhashed_password\nfull_name\nis_active\ncreated_at")
    
    draw_box(4.0, 3.2, 2.4, 1.6, "PROFILES", "id (PK)\nuser_id (FK)\nmonthly_income\nmonthly_expenses\nemployment_type\ncredit_score")
    draw_box(4.0, 0.5, 2.4, 2.0, "LOANS", "id (PK)\nuser_id (FK)\nloan_type\nlender_name\nloan_amount\noutstanding_balance\nloan_status")
    
    draw_box(8.0, 3.4, 2.2, 1.4, "AI_RESPONSES", "id (PK)\nuser_id (FK)\nprompt_type\nmodel_used\ntokens_used")
    draw_box(8.0, 0.5, 2.5, 1.8, "SETTLEMENT_HISTORY", "id (PK)\nuser_id (FK)\nloan_id (FK)\nsettlement_percentage\nsettlement_amount\nstrategy_json\nai_generated")
    
    draw_box(11.5, 3.4, 2.2, 1.4, "ACTIVITY_LOGS", "id (PK)\nuser_id (FK)\naction\nentity_type\nentity_id")
    draw_box(11.5, 0.5, 2.5, 1.6, "NEGOTIATION_HISTORY", "id (PK)\nuser_id (FK)\nloan_id (FK)\nlender_name\nletter_content\nai_generated")

    # Relationships from USERS
    draw_rel(2.7, 2.6, 4.0, 4.0, "1 : 1", rad=-0.1) # to Profile
    draw_rel(2.7, 2.6, 4.0, 1.5, "1 : N", rad=0.1)  # to Loans
    draw_rel(2.7, 2.6, 8.0, 4.1, "1 : N", rad=-0.2) # to AI Responses
    draw_rel(2.7, 2.6, 8.0, 1.4, "1 : N", rad=0.1)  # to Settlement
    draw_rel(2.7, 2.6, 11.5, 4.1, "1 : N", rad=-0.3) # to Activity
    draw_rel(2.7, 2.6, 11.5, 1.3, "1 : N", rad=0.2)  # to Negotiation

    # Relationships from LOANS
    draw_rel(6.4, 1.5, 8.0, 1.4, "1 : N") # to Settlement
    draw_rel(6.4, 1.5, 11.5, 1.3, "1 : N", rad=0.1) # to Negotiation

    plt.tight_layout()
    plt.savefig('documentation/7.Project Documentation/ER_Diagram.png', dpi=300, bbox_inches='tight')
    print("Generated ER_Diagram.png")

create_architecture_diagram()
create_er_diagram()
