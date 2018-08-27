import javalang
from file_controller import FileController

#fc = FileController("")
#file_list = fc.get_file_list()
tree = javalang.parse.parse("package visitor;"
                            "import Node.ParsingNode;"
                            "import com.github.javaparser.ast.visitor.VoidVisitorAdapter;"
                            "import java.util.ArrayList;public class IEEEStructVisitor extends VoidVisitorAdapter<Integer> "
                            "{ private ArrayList<ParsingNode> parsingNodes = new ArrayList<>(); public ArrayList<ParsingNode> getParsingNodes() { return parsingNodes;}}")

for path, node in tree:
    print(path)
