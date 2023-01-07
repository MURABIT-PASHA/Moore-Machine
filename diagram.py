from diagrams import Diagram, Edge, Node
class ImageDiagram:
    def __init__(self, diagram:dict, state_number:int, alphabet:list):
        self.diagram = diagram
        self.state_number = state_number
        self.alphabet = alphabet
        self._image_name = "moore"
    def _create_diagram(self):
        state_number = self.state_number
        alphabet = self.alphabet
        diagram = self.diagram
        with Diagram("Moore Machine", show=False, direction="LR", filename=self._image_name, outformat="jpg", curvestyle="ortho"):
            state_node_list = []
            for a in range(state_number):
                state_node_list.append(Node(label=f"q{a}/{diagram[f'q{a}']['output']}", shape="circle", height=".25", ))
            for b in range(state_number):
                for c in alphabet:
                    state_node_list[b].connect(state_node_list[int(diagram[f'q{b}'][f'{c}'].replace("q", ""))],
                                               edge=Edge(color="red", label=f"{c}",
                                                         forward=True, fontsize="15"))
    def get_image_path(self) -> str:
        self._create_diagram()
        return self._image_name + ".jpg"