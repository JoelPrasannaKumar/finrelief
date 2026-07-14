import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_architecture_diagram():
    fig, ax = plt.subplots(figsize=(15.5, 4.5))
    ax.set_xlim(0, 15.5)
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
    plt.savefig('Architecture_Diagram.png', dpi=300, bbox_inches='tight')
    print("Generated Architecture_Diagram.png")

create_architecture_diagram()
