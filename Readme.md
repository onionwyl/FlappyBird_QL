## Flappy bird Q-learning

* 目前暂时的模型
	* 状态
		* 距离下个下侧柱子右边的x轴和y轴距离差dx,dy
	* 动作
		* 飞或不飞 1和0
	* Reward
		* 状态为alive奖励1,死亡奖励-1000
	* 模型训练暂时有一些问题，修改中
	    * 问题在于将连续的几帧当作一帧来判断，有时会出现判断错误导致Q table更新错误，正在尝试写DQN版本
    * 模型在qlBot.py中，如需自行建立模型，可根据qlBot_example.py进行修改
    * 训练好的模型在Q.json和Q1.json中，暂时可飞50次+左右
* 参考资料
	* [python版flappy bird](https://github.com/sourabhv/FlapPyBird)
	* js版flappy bird ql
		* http://sarvagyavaish.github.io/FlappyBirdRL/
		* https://enhuiz.github.io/flappybird-ql/
