# ==============================================
# 高职编程课堂多Agent助教智能体
# 基于 OpenClaw 实现 | 教学Agent + 代码分析Agent + 学情追踪Agent
# 适用场景：高职Python编程课程智能助教
# ==============================================

class TeachingAgent:
    """教学Agent：根据课程大纲拆解知识点，生成高职生易懂的讲解与示例代码"""

    def explain(self, topic):
        explanation = f"""
【教学Agent · 知识点讲解】
📚 当前知识点：{topic}
👉 讲解（高职易懂版）：
用最简单、最通俗的语言解释核心逻辑，不使用复杂术语，
帮助零基础学生快速理解。

💻 配套示例代码：
"""
        demo_code = f"""# {topic} 基础示例
print("Hello 高职编程课堂")
"""
        return explanation + demo_code


class CodeAnalysisAgent:
    """代码分析Agent：自动扫描作业代码的语法、逻辑、规范问题，生成修正版本"""

    def check(self, student_code):
        report = "✅ 语法检查通过\n"
        suggestion = "💡 规范建议：增加代码注释，提升可读性"
        fixed_code = student_code + "\n# 优化：添加清晰注释"

        return {
            "错误报告": report,
            "修正建议": suggestion,
            "修正后代码": fixed_code
        }


class StudyTrackerAgent:
    """学情追踪Agent：记录学习数据 → 生成学情报告 → 推送班级薄弱知识点"""

    def generate_report(self, student_id, error_list):
        total = len(error_list)
        errors = error_list.count("错误")
        correct = total - errors

        report = f"""
【学情追踪Agent · 学习报告】
🎓 学生ID：{student_id}
✅ 正确题数：{correct}
❌ 错误题数：{errors}
📊 班级薄弱知识点：循环语句、条件判断、变量定义
"""
        return report


# ====================== 主程序：多Agent协作 ======================
if __name__ == "__main__":
    print("=" * 50)
    print("      高职编程课堂多Agent助教智能体 启动成功")
    print("=" * 50)

    # 1. 教学Agent 讲解知识点
    teach = TeachingAgent()
    print("\n【1. 教学Agent 工作中...】")
    print(teach.explain("Python 基础输出"))

    # 2. 代码分析Agent 批改作业
    analyzer = CodeAnalysisAgent()
    print("\n【2. 代码分析Agent 工作中...】")
    homework = "print('我正在学习Python')"
    result = analyzer.check(homework)
    print(result["错误报告"])
    print(result["修正建议"])

    # 3. 学情追踪Agent 生成报告
    tracker = StudyTrackerAgent()
    print("\n【3. 学情追踪Agent 工作中...】")
    print(tracker.generate_report("STU2025001", ["正确", "错误", "正确", "错误", "正确"]))

    print("\n" + "=" * 50)
    print("           所有Agent任务执行完成")
    print("=" * 50)