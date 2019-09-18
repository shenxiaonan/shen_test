import allure


class TestJenkins:
    @allure.step('测试步骤~')
    def test_001(self):
        allure.attach('附件名称不想写', '附件内容不想写')
        assert True
