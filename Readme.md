## Flappy bird Q-learning

* 目前暂时的模型
	* 状态
		* 距离下个下侧柱子右边的x轴和y轴距离差dx,dy
	* 动作
		* 飞或不飞 1和0
	* Reward
		* 状态为alive奖励1,死亡奖励-1000
	* 模型训练暂时有一些问题，修改中
* 参考资料
	* [python版flappy bird](https://github.com/sourabhv/FlapPyBird)
	* js版flappy bird ql
		* http://sarvagyavaish.github.io/FlappyBirdRL/
		* https://enhuiz.github.io/flappybird-ql/
