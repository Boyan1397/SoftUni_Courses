from typing import List

from project.campaigns.base_campaign import BaseCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    INFLUENCER_TYPES = {"PremiumInfluencer": PremiumInfluencer, "StandardInfluencer": StandardInfluencer}
    CAMPAIGN_TYPES = {"HighBudgetCampaign": HighBudgetCampaign, "LowBudgetCampaign": LowBudgetCampaign}

    def __init__(self):
        self.influencers: List[BaseInfluencer] = []
        self.campaigns: List[BaseCampaign] = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in self.INFLUENCER_TYPES:
            return f"{influencer_type} is not an allowed influencer type."

        for inf in self.influencers:
            if inf.username == username:
                return f"{username} is already registered."

        current_influencer = InfluencerManagerApp.INFLUENCER_TYPES[influencer_type](username, followers, engagement_rate)
        self.influencers.append(current_influencer)
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.CAMPAIGN_TYPES:
            return f"{campaign_type} is not a valid campaign type."

        for cam in self.campaigns:
            if cam.campaign_id == campaign_id:
                return f"Campaign ID {campaign_id} has already been created."

        current_campaign = InfluencerManagerApp.CAMPAIGN_TYPES[campaign_type](campaign_id, brand, required_engagement)
        self.campaigns.append(current_campaign)
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        try:
            influencer = [inf for inf in self.influencers if influencer_username == inf.username][0]
        except IndexError:
            return f"Influencer '{influencer_username}' not found."

        try:
            campaign = [cam for cam in self.campaigns if cam.campaign_id == campaign_id][0]
        except IndexError:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."

        payment = influencer.calculate_payment(campaign)
        if payment > 0.0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= payment
            influencer.campaigns_participated.append(campaign)
            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self):
        total_reached_followers = {}
        for campaign in self.campaigns:
            reached_followers = sum(influencer.reached_followers(campaign.__class__.__name__)
                                    for influencer in campaign.approved_influencers)
            if reached_followers > 0:
                total_reached_followers[campaign] = reached_followers
        return total_reached_followers

    def influencer_campaign_report(self, username: str) -> str:
        influencer = next((i for i in self.influencers if i.username == username), None)
        if not influencer:
            return f"Influencer '{username}' not found."

        return influencer.display_campaigns_participated()

    def campaign_statistics(self) -> str:
        stats = []
        for campaign in sorted(self.campaigns, key=lambda c: (len(c.approved_influencers), -c.budget)):
            total_reached_followers = sum(
                influencer.reached_followers(campaign.__class__.__name__)
                for influencer in campaign.approved_influencers
            )
            stats.append(
                f"  * Brand: {campaign.brand}, Total influencers: {len(campaign.approved_influencers)}, Total budget: ${campaign.budget:.2f}, Total reached followers: {total_reached_followers}"
            )
        return "$$ Campaign Statistics $$\n" + "\n".join(stats)