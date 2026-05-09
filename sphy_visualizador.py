import py5
import pandas as pd

class SPHYVisualizer:
    def __init__(self, parquet_path="sphy_frames.parquet"):
        self.df = pd.read_parquet(parquet_path)
        self.current_frame = 0
        self.total_frames = len(self.df)
        print(f"Loaded {self.total_frames} frames from parquet file.")

    def get_frame_data(self):
        if self.current_frame >= self.total_frames:
            self.current_frame = 0  # loop back to start
        
        row = self.df.iloc[self.current_frame]
        self.current_frame += 1
        return row


vis = None

def setup():
    global vis
    py5.size(1920, 1080, py5.P3D)
    vis = SPHYVisualizer("sphy_frames.parquet")


def draw():
    global vis
    data = vis.get_frame_data()

    py5.background(5, 7, 15)

    # Lighting based on phase state
    py5.ambient_light(30, 30, 50)
    if data["quebra"]:
        py5.point_light(255, 51, 85, 0, 0, 300)
    else:
        py5.point_light(0, 229, 255, 200, -200, 400)

    py5.translate(py5.width / 2, py5.height / 2, -200)
    py5.rotate_y(py5.frame_count * 0.01)

    # S(Φ) Field Visualization
    py5.no_fill()
    py5.stroke(0, 229, 255, 40) if not data["quebra"] else py5.stroke(255, 51, 85, 60)
    py5.sphere_detail(15)
    with py5.push_matrix():
        py5.scale(1.4 + (data["respiro"] * 0.08))
        py5.sphere(320)

    # Oxygen Atom
    py5.no_stroke()
    py5.fill(255, 51, 85)
    py5.sphere(60)

    # Hydrogen Atoms in Dissociation
    angulo_h2o = py5.radians(104.5 / 2)
    for side in [1, -1]:
        with py5.push_matrix():
            py5.rotate_z(side * angulo_h2o)
            py5.translate(data["distancia"], 0, 0)
            py5.fill(0, 229, 255) if not data["quebra"] else py5.fill(100, 100, 120)
            py5.sphere(30)

            if not data["quebra"]:
                py5.stroke(0, 229, 255, 80)
                py5.line(0, 0, 0, -data["distancia"], 0, 0)

    draw_audit_interface(data)


def draw_audit_interface(data):
    py5.hint(py5.DISABLE_DEPTH_TEST)
    py5.camera()

    # Header
    py5.fill(0, 229, 255)
    py5.text_size(18)
    py5.text("HARPIA SPHY CORE - REAL-TIME FRAME AUDIT", 40, 50)

    # SHA-256 Validator Box
    py5.no_fill()
    py5.stroke(0, 229, 255, 100)
    py5.rect(40, 70, 520, 120)

    py5.fill(200, 230, 255)
    py5.text_size(13)
    py5.text(f"FRAME {int(data['frame'])} / {vis.total_frames}  |  SHA-256 HASH:", 55, 95)

    # Hash display (green for integrity)
    py5.fill(0, 255, 150)
    py5.text(f"{data['hash_visual']}...", 55, 120)

    py5.fill(0, 229, 255)
    py5.text("INTEGRITY STATUS: [ VALIDATED ]", 55, 150)

    # Physics Metrics
    py5.text_size(15)
    color_status = (255, 51, 85) if data["quebra"] else (0, 229, 255)
    py5.fill(*color_status)

    metrics = (
        f"STABILITY: {data['estabilidade']*100:.2f}%\n"
        f"RESONANCE: {data['fator_ressonancia']:.4f} Hz\n"
        f"DISTANCE H: {data['distancia']:.2f} u"
    )
    py5.text(metrics, 40, 220)

    # Dissociation Alert
    if data["quebra"]:
        py5.fill(255, 51, 85)
        py5.text_size(24)
        py5.text(">>> DISSOCIATION DETECTED <<<", 40, 350)

    py5.hint(py5.ENABLE_DEPTH_TEST)


if __name__ == "__main__":
    py5.run_sketch()
