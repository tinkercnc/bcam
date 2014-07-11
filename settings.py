from tool import Tool, ToolType
class LineType:
    def __init__(self, lw, selected_lw, color, selected_color):
        self.lw = lw
        self.selected_lw = selected_lw
        self.color = color
        self.selected_color = selected_color

    def set_lt(self, ctx):
        if len(self.color) == 3:
            ctx.set_source_rgb(self.color[0], self.color[1], self.color[2])
        else:
            ctx.set_source_rgba(self.color[0], self.color[1], self.color[2], self.color[3])
        ctx.set_line_width(self.lw)

    def set_selected_lt(self, ctx):
        if len(self.selected_color) == 3:
            ctx.set_source_rgb(self.selected_color[0], self.selected_color[1], self.selected_color[2])
        else:
            ctx.set_source_rgba(self.selected_color[0], self.selected_color[1], self.selected_color[2], self.selected_color[3])
        ctx.set_line_width(self.selected_lw)

class Settings:
    def __init__(self):
        self.line_types = {"default": LineType(0.2, 0.5, (0,0,0), (1,0,0))}
        self.tool = Tool("cylinder", ToolType.cylinder)
        self.select_box_lt = LineType(0.1, 0.1, (0, 1, 0, 0.2), (0, 1, 0, 0.2))

    def get_lt(self, name):
        return self.line_types[name]
        
    def get_def_lt(self):
        return self.line_types["default"]

settings = Settings()