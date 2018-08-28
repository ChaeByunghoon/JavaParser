import javalang
from javalang.tree import *

class IEEEVisitor:

    def __init__(self, code):
        self.code = code

    def parse_tree(self):
        self.tree = javalang.parse.parse(self.code)
        node_list = list()
        for _, node in self.tree:
            if isinstance(node, CompilationUnit):
                node_list.append(node)
            elif isinstance(node, FormalParameter):
                node_list.append(node)
            elif isinstance(node, BasicType):
                node_list.append(node)
            elif isinstance(node, PackageDeclaration):
                node_list.append(node.name)
            elif isinstance(node, InterfaceDeclaration):
                node_list.append(node.name)
            elif isinstance(node, CatchClauseParameter):
                node_list.append(node)
            elif isinstance(node, ClassDeclaration):
                node_list.append(node.name)
            elif isinstance(node, MethodInvocation):
                node_list.append(node.member)
            elif isinstance(node, SuperMethodInvocation):
                node_list.append(node.member)
            elif isinstance(node, MemberReference):
                node_list.append(node)
            elif isinstance(node, SuperMemberReference):
                node_list.append(node)
            elif isinstance(node, ConstructorDeclaration):
                node_list.append(node.name)
            elif isinstance(node, ReferenceType):
                node_list.append(node)
            elif isinstance(node, MethodDeclaration):
                node_list.append(node.name)
            elif isinstance(node, VariableDeclarator):
                node_list.append(node)
            elif isinstance(node, IfStatement):
                node_list.append(node)
            elif isinstance(node, WhileStatement):
                node_list.append(node)
            elif isinstance(node, DoStatement):
                node_list.append(node)
            elif isinstance(node, ForStatement):
                node_list.append(node)
            elif isinstance(node, AssertStatement):
                node_list.append(node)
            elif isinstance(node, BreakStatement):
                node_list.append(node)
            elif isinstance(node, ContinueStatement):
                node_list.append(node)
            elif isinstance(node, ReturnStatement):
                node_list.append(node)
            elif isinstance(node, ThrowStatement):
                node_list.append(node)
            elif isinstance(node, SynchronizedStatement):
                node_list.append(node)
            elif isinstance(node, TryStatement):
                node_list.append(node)
            elif isinstance(node, SwitchStatement):
                node_list.append(node)
            elif isinstance(node, BlockStatement):
                node_list.append(node)
            elif isinstance(node, StatementExpression):
                node_list.append(node)
            elif isinstance(node, TryResource):
                node_list.append(node)
            elif isinstance(node, CatchClause):
                node_list.append(node)
            elif isinstance(node, SwitchStatementCase):
                node_list.append(node)
            elif isinstance(node, ForControl):
                node_list.append(node)
            elif isinstance(node, EnhancedForControl):
                node_list.append(node)

        return node_list