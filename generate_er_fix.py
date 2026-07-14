import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_er_diagram():
    fig, ax = plt.subplots(figsize=(15, 7.5))
    ax.set_xlim(0, 15)
    ax.set_ylim(-0.5, 7.0)
    ax.axis('off')

    def draw_box(x, y, w, h, title, fields):
        rect_head = patches.Rectangle((x, y+h-0.4), w, 0.4, linewidth=1, edgecolor='black', facecolor='#b4c6e7', zorder=2)
        ax.add_patch(rect_head)
        ax.text(x + w/2, y+h-0.2, title, ha='center', va='center', fontsize=10, fontweight='bold', zorder=3)
        
        rect_body = patches.Rectangle((x, y), w, h-0.4, linewidth=1, edgecolor='black', facecolor='#e9eef7', zorder=2)
        ax.add_patch(rect_body)
        ax.text(x + 0.1, y + (h-0.4)/2, fields, ha='left', va='center', fontsize=8, linespacing=1.6, zorder=3)
        return (x, x+w, y, y+h)

    def draw_polyline(points, label="1:N"):
        xs = [p[0] for p in points]
        ys = [p[1] for p in points]
        ax.plot(xs, ys, color='black', lw=1.5, zorder=1)
        # Arrow head at the end
        ax.annotate("", xy=(xs[-1], ys[-1]), xytext=(xs[-2], ys[-2]), 
                    arrowprops=dict(arrowstyle="-|>", color="black", lw=1.5), zorder=1)
        
        # Label at the first horizontal segment
        if len(points) >= 2:
            lx = (xs[0] + xs[1]) / 2
            ly = (ys[0] + ys[1]) / 2
            ax.text(lx, ly, label, ha='center', va='bottom', fontsize=8, color='#d32f2f', fontweight='bold', bbox=dict(facecolor='white', edgecolor='none', alpha=0.8, pad=1), zorder=4)

    # Entities
    b_users = draw_box(0.5, 2.5, 2.2, 1.6, "USERS", "id (PK)\nemail\nhashed_password\nfull_name\nis_active\ncreated_at")

    b_prof = draw_box(4.0, 4.6, 2.4, 1.6, "PROFILES", "id (PK)\nuser_id (FK)\nmonthly_income\nmonthly_expenses\nemployment_type\ncredit_score")
    b_ai = draw_box(7.5, 4.6, 2.2, 1.4, "AI_RESPONSES", "id (PK)\nuser_id (FK)\nprompt_type\nmodel_used\ntokens_used")
    b_act = draw_box(11.0, 4.6, 2.2, 1.4, "ACTIVITY_LOGS", "id (PK)\nuser_id (FK)\naction\nentity_type\nentity_id")

    b_loans = draw_box(4.0, 0.4, 2.4, 1.8, "LOANS", "id (PK)\nuser_id (FK)\nloan_type\nlender_name\nloan_amount\noutstanding_balance\nloan_status")
    b_sett = draw_box(7.5, 0.4, 2.5, 1.8, "SETTLEMENT_HISTORY", "id (PK)\nuser_id (FK)\nloan_id (FK)\nsettlement_percentage\nsettlement_amount\nstrategy_json\nai_generated")
    b_nego = draw_box(11.0, 0.4, 2.5, 1.6, "NEGOTIATION_HISTORY", "id (PK)\nuser_id (FK)\nloan_id (FK)\nlender_name\nletter_content\nai_generated")

    # USERS to PROFILES
    draw_polyline([(2.7, 3.7), (3.3, 3.7), (3.3, 5.4), (4.0, 5.4)], "1 : 1")

    # USERS to AI_RESPONSES (goes way up over PROFILES)
    draw_polyline([(2.5, 4.1), (2.5, 6.4), (8.6, 6.4), (8.6, 6.0)], "1 : N")

    # USERS to ACTIVITY_LOGS (goes even higher)
    draw_polyline([(2.3, 4.1), (2.3, 6.6), (12.1, 6.6), (12.1, 6.0)], "1 : N")

    # USERS to LOANS
    draw_polyline([(2.7, 2.9), (3.3, 2.9), (3.3, 1.3), (4.0, 1.3)], "1 : N")

    # USERS to SETTLEMENT_HISTORY (goes way down under LOANS)
    draw_polyline([(2.5, 2.5), (2.5, 0.1), (8.75, 0.1), (8.75, 0.4)], "1 : N")

    # USERS to NEGOTIATION_HISTORY (goes even lower)
    draw_polyline([(2.3, 2.5), (2.3, -0.2), (12.25, -0.2), (12.25, 0.4)], "1 : N")

    # LOANS to SETTLEMENT_HISTORY
    draw_polyline([(6.4, 1.3), (7.5, 1.3)], "1 : N")

    # LOANS to NEGOTIATION_HISTORY (goes above SETTLEMENT_HISTORY)
    draw_polyline([(6.4, 1.8), (6.8, 1.8), (6.8, 2.4), (12.25, 2.4), (12.25, 2.0)], "1 : N")

    plt.tight_layout()
    plt.savefig('ER_Diagram.png', dpi=300, bbox_inches='tight')
    print("Generated ER_Diagram.png")

create_er_diagram()
