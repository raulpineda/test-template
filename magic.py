import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

class AutoViz:
    def __init__(self):
        print("🚀 Initializing AutoViz...")
        
    def generate_sample_data(self):
        """Generate exciting sample data for demonstration"""
        # Create date range
        dates = [datetime.now() - timedelta(days=x) for x in range(30)]
        
        # Generate synthetic metrics
        metrics = {
            'user_growth': np.random.exponential(scale=100, size=30) * 1.5,
            'engagement': np.random.normal(loc=75, scale=15, size=30),
            'performance': np.random.gamma(shape=2, scale=20, size=30)
        }
        
        return pd.DataFrame(metrics, index=dates)
    
    def create_visualization(self):
        """Create an eye-catching visualization"""
        print("✨ Creating visualization masterpiece...")
        
        data = self.generate_sample_data()
        
        # Create a modern-looking plot
        plt.style.use('dark_background')
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Plot with gradient colors
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
        for col, color in zip(data.columns, colors):
            ax.plot(data.index, data[col], label=col.replace('_', ' ').title(), 
                   color=color, linewidth=2, alpha=0.8)
            
        # Add some pizzazz
        ax.set_title('Dynamic Metrics Dashboard 📈', fontsize=16, pad=20)
        ax.grid(True, alpha=0.2)
        ax.legend(frameon=False)
        
        # Style tweaks
        plt.tight_layout()
        return fig

if __name__ == "__main__":
    print("🌟 Welcome to AutoViz Demo!")
    viz = AutoViz()
    
    print("🔮 Detecting patterns...")
    fig = viz.create_visualization()
    
    print("✅ Visualization complete! Displaying results...")
    plt.show()
    
    print("🎉 Demo completed successfully!")
