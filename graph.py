from langgraph.graph import END,START,StateGraph
from nodes import parse_resume, analyze_jd, rewrite_resume, generate_cv, score_fit
from state import AgentState

graph = StateGraph(AgentState)

graph.add_node("parse_resume", parse_resume)
graph.add_node("analyze_jd", analyze_jd)
graph.add_node("rewrite_resume", rewrite_resume)
graph.add_node("generate_cv", generate_cv)
graph.add_node("score_fit", score_fit)

graph.add_edge(START, "parse_resume")

graph.add_edge("parse_resume", "analyze_jd")
graph.add_edge("analyze_jd", "rewrite_resume")
graph.add_edge("analyze_jd", "generate_cv")
graph.add_edge("analyze_jd", "score_fit")

graph.add_edge("rewrite_resume", END)
graph.add_edge("generate_cv", END)
graph.add_edge("score_fit", END)

app = graph.compile()

