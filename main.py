from ieee_visitor import IEEEVisitor
from file_controller import FileController
import javalang
import sys
"""
visitor = IEEEVisitor(("package visitor;"
                            "import Node.ParsingNode;"
                            "import com.github.javaparser.ast.visitor.VoidVisitorAdapter;"
                            "import java.util.ArrayList;public class IEEEStructVisitor extends VoidVisitorAdapter<Integer> "
                            "{ private ArrayList<ParsingNode> parsingNodes = new ArrayList<>(); public ArrayList<ParsingNode> getParsingNodes() { parsingNodes.remove();return parsingNodes;}}"))

"""
fc = FileController("/Users/chaebyeonghun/Desktop/RTSE/source_result/camel-1.4/"
                    , "/Users/chaebyeonghun/Desktop/IEEEData/")

file_list = fc.get_path_file_list()

source_list = fc.read_files(file_list)

output_list = list()

for i in range(0, len(source_list)):
    visitor = IEEEVisitor(source_list[i])
    try:
        parsed_tree = visitor.parse_tree()
        output_list.append(parsed_tree)
    except javalang.tokenizer.LexerError:
        print("Error")
        print(file_list[i])

fc.file_out(fc.get_output_path_list(), output_list)
